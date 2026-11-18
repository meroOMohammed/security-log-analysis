# Security Log Analysis & Incident Investigation Report

## Project Overview
This project demonstrates a security log analysis and incident investigation workflow using Python and Pandas on a synthetic security log dataset.

The objective is to identify suspicious authentication activities, investigate potentially malicious patterns, build an event timeline, and provide actionable security recommendations.

## Dataset
- Source: Synthetic test dataset
- Records analyzed: 4,858
- Time period: November 1–7, 2026
- Hosts: 5
- Users: 19

**Note:** All data is fictional and used for educational and portfolio demonstration purposes. This report does not describe a real security incident.

## Analysis Highlights
- Analyzed successful and failed login attempts.
- Investigated repeated authentication failures followed by a successful login.
- Examined suspicious SSH username-guessing activity.
- Identified potential password-spraying patterns.
- Reviewed unusual successful login activity and subsequent account changes.
- Developed an event timeline and security recommendations.

## Tools & Technologies
- Python
- Pandas
- Security Log Analysis
- Incident Investigation
- SOC Analysis

## Key Findings
The analysis highlighted several suspicious authentication patterns that may require further investigation in a real environment, including repeated failed logins, possible password guessing, and unusual login activity.

These findings are indicators for investigation, not proof of compromise.

## Recommendations
- Enforce Multi-Factor Authentication (MFA).
- Apply account lockout and authentication policies.
- Restrict and monitor remote access services such as SSH.
- Review privileged account activity.
- Monitor unusual login patterns and investigate relevant indicators.

## Project Deliverables
- Security Log Analysis Report (PDF)
- Selected report screenshots
- Synthetic dataset (if included)

## Disclaimer
This is an educational portfolio project based on fictional data. IP addresses, usernames, and host information are illustrative. No external threat-intelligence or IP reputation validation is claimed.

**Prepared by:** Mirvet Mohamed
