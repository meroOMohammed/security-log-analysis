# Security Log Analysis & Incident Investigation

A SOC-style investigation of one week of authentication and access logs: a Python script that applies detection rules with Pandas, and a written incident report with findings and recommendations.

> **Note:** the log file is a **simulated dataset** prepared for practice. All IP addresses, hostnames and usernames are fictional. This is a learning project, not a real incident.

## What is in this repo

| Path | Description |
|---|---|
| `analyze_logs.py` | Detection script (Python + Pandas) |
| `sample_security_logs.csv` | Sample logs: 4,858 events, 2026-11-01 to 2026-11-07, 5 hosts, 19 accounts |
| `report/security_log_analysis_report.pdf` | Full investigation report (Arabic) |
| `requirements.txt` | Python dependencies |

## How to run

```bash
pip install -r requirements.txt
python analyze_logs.py                      # picks up the CSV next to the script
python analyze_logs.py path/to/your_logs.csv
```

Expected CSV columns: `timestamp, source_ip, username, event_type, status, host, user_agent, dest_port, failure_reason`

The script prints its output in Arabic.

## Detections

| # | Rule | Default threshold |
|---|---|---|
| 1 | Event and login overview (success vs. failed) | n/a |
| 2 | Top source IPs by failed logins | n/a |
| 3 | Brute force | 10+ failed logins from one IP within 5 minutes |
| 4 | Password spraying | one IP failing against 5+ distinct usernames |
| 5 | Successful login after a failure streak | possible compromise |
| 6 | Successful login from outside the internal range (not `10.x`) | n/a |
| 7 | Successful logins between 00:00 and 05:00 | n/a |
| 8 | Account lockouts | n/a |

Thresholds can be tuned to the environment.

## Findings summary

| # | Activity | Source IP | Severity |
|---|---|---|---|
| 1 | Brute force followed by a successful login to `admin` (possible compromise) | 185.220.101.45 | Critical |
| 2 | SSH username guessing | 45.155.205.233 | High |
| 3 | Password spraying across all accounts | 103.77.192.18 | High |
| 4 | Successful external login at 03:22 followed by a password change | 91.240.118.77 | High |
| 5 | Two account lockouts from internal addresses (likely user error) | internal | Low |

The full report covers each case in detail, with recommendations split into immediate (24 hours), short-term (2 weeks) and long-term actions.

## Limitations

- IP reputation and geolocation were not checked, and no external sources were used.
- Results are indicators that need verification, not proof of attacker intent or impact.

## Skills demonstrated

Log analysis, detection logic (brute force, spraying, anomalous access), incident triage and severity rating, and report writing with actionable recommendations.
