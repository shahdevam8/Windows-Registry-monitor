import winreg
import json
import time
from datetime import datetime

# ---------------- CONFIG ---------------- #

MONITOR_KEYS = {
    "HKCU_RUN": (winreg.HKEY_CURRENT_USER,
                 r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "HKLM_RUN": (winreg.HKEY_LOCAL_MACHINE,
                 r"Software\Microsoft\Windows\CurrentVersion\Run"),
}

BASELINE_FILE = "baseline.json"
LOG_FILE = "registry_logs.txt"
REPORT_FILE = "report.txt"
INTERVAL = 30  # seconds

# ---------------- UTILITIES ---------------- #

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    print(entry.strip())

    with open(LOG_FILE, "a") as f:
        f.write(entry)

def read_registry():
    snapshot = {}

    for key_name, (hive, path) in MONITOR_KEYS.items():
        snapshot[key_name] = {}

        try:
            with winreg.OpenKey(hive, path, 0, winreg.KEY_READ) as key:
                i = 0
                while True:
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        snapshot[key_name][name] = value
                        i += 1
                    except OSError:
                        break
        except Exception as e:
            log(f"ERROR reading {key_name}: {e}")

    return snapshot

def save_baseline(data):
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline():
    try:
        with open(BASELINE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# ---------------- DETECTION ---------------- #

def analyze_changes(baseline, current):
    alerts = []

    for key in current:
        base_items = baseline.get(key, {})
        curr_items = current[key]

        # New entries
        for name in curr_items:
            if name not in base_items:
                alerts.append(
                    f"NEW AUTORUN ENTRY: {name} -> {curr_items[name]}"
                )

        # Removed entries
        for name in base_items:
            if name not in curr_items:
                alerts.append(
                    f"REMOVED AUTORUN ENTRY: {name}"
                )

        # Modified entries
        for name in curr_items:
            if name in base_items and curr_items[name] != base_items[name]:
                alerts.append(
                    f"MODIFIED ENTRY: {name}\n"
                    f"OLD: {base_items[name]}\n"
                    f"NEW: {curr_items[name]}"
                )

    return alerts

def write_report(alerts):
    with open(REPORT_FILE, "a") as f:
        f.write("\n" + "=" * 50 + "\n")
        f.write("REGISTRY CHANGE DETECTION REPORT\n")
        f.write("=" * 50 + "\n")
        for alert in alerts:
            f.write(alert + "\n")

# ---------------- MAIN LOOP ---------------- #

def main():
    log("Windows Registry Monitoring Agent Started")

    baseline = load_baseline()
    if not baseline:
        log("Baseline not found. Creating baseline...")
        baseline = read_registry()
        save_baseline(baseline)
        log("Baseline created. Restart program to begin monitoring.")
        return

    try:
        while True:
            current = read_registry()
            alerts = analyze_changes(baseline, current)

            if alerts:
                log(f"{len(alerts)} registry change(s) detected")
                for alert in alerts:
                    log(alert)
                write_report(alerts)

                # Update baseline after detection
                save_baseline(current)
                baseline = current

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        log("Monitoring stopped by user")

# ---------------- ENTRY ---------------- #

if __name__ == "__main__":
    main()
