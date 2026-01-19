import csv
from datetime import datetime

LOG_FILE = "registry_logs.csv"
REPORT_FILE = "final_report.txt"

def log_event(timestamp, key, old, new, severity, reason):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, key, old, new, severity, reason])

def write_final_report(summary):
    with open(REPORT_FILE, "w") as f:
        f.write("Windows Registry Monitoring Report\n")
        f.write("=" * 40 + "\n\n")
        for item in summary:
            f.write(item + "\n")
