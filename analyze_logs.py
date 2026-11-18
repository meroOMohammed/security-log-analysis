import sys
import os
import pandas as pd

# المسار: لو كتبتيه في الأمر بياخده، وإلا بيدور على أي ملف csv جنب السكريبت
import glob
folder = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    found = sorted(glob.glob(os.path.join(folder, "sample_security_logs*.csv")))
    found = found or sorted(glob.glob(os.path.join(folder, "*.csv")))
    if not found:
        print("ما لقيتش ملف csv في الفولدر ده:", folder)
        print("نزّلي ملف السجلات وحطيه جنب السكريبت، أو اكتبي مساره بعد اسم السكريبت.")
        sys.exit(1)
    path = found[0]
print("بقرا الملف:", path)

df = pd.read_csv(path, parse_dates=["timestamp"])
logins = df[df.event_type == "login"]

print("=== 1) ملخص عام ===")
print("عدد السجلات:", len(df), "| من", df.timestamp.min(), "إلى", df.timestamp.max())
print(df.event_type.value_counts().to_string())

print("\n=== 2) ناجح مقابل فاشل ===")
print(logins.status.value_counts().to_string())

print("\n=== 3) أكتر العناوين فشلاً ===")
failed = logins[logins.status == "failed"]
top_fail = failed.groupby("source_ip").agg(failed=("status","size"), users=("username","nunique"),
                                           first=("timestamp","min"), last=("timestamp","max"))
print(top_fail.sort_values("failed", ascending=False).head(8).to_string())

print("\n=== 4) تخمين كلمة السر: 10+ فشل خلال 5 دقايق من نفس العنوان ===")
bf = []
for ip, g in failed.sort_values("timestamp").groupby("source_ip"):
    s = g.set_index("timestamp").status.rolling("5min").count()
    if s.max() >= 10:
        bf.append((ip, int(s.max()), s.idxmax()))
for r in bf: print(r)

print("\n=== 5) رش كلمات السر: عنوان واحد على 5+ مستخدمين ===")
print(top_fail[top_fail.users >= 5][["failed","users"]].to_string())

print("\n=== 6) نجاح بعد سلسلة فشل (احتمال اختراق) ===")
for ip,_,_ in bf:
    g = logins[logins.source_ip == ip].sort_values("timestamp")
    succ = g[g.status == "success"]
    if len(succ): print(ip, "نجح على", succ.username.iloc[0], "الساعة", succ.timestamp.iloc[0])

print("\n=== 7) دخول ناجح من عنوان خارجي (مش 10.x) ===")
ext = logins[(logins.status=="success") & (~logins.source_ip.str.startswith("10."))]
print(ext[["timestamp","source_ip","username","host"]].to_string(index=False))

print("\n=== 8) دخول ناجح بين 12 بالليل و5 الفجر ===")
night = logins[(logins.status=="success") & (logins.timestamp.dt.hour < 5)]
print(night.groupby("username").size().sort_values(ascending=False).head(5).to_string())

print("\n=== 9) قفل حسابات ===")
print(df[df.event_type=="account_lockout"][["timestamp","username","source_ip"]].to_string(index=False))
