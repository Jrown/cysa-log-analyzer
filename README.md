# cysa-log-analyzer
cybersecurity project to detect failed SSH login attempts from auth.log
yber Log Analyzer

A simple Python-based cybersecurity mini-project that scans Linux auth logs and flags suspicious login attempts (failed SSH logins).
 Reads from `auth.log`
- Detects `Failed password` entries (common brute-force attempts)
- Prints suspicious entries to the terminal
