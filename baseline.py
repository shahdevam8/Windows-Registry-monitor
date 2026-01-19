import winreg
import hashlib
import json
import os

BASELINE_FILE = "baseline.json"

def hash_value(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

def capture_registry_snapshot(monitored_keys):
    snapshot = {}

    for hive, path in monitored_keys:
        try:
            key = winreg.OpenKey(hive, path)
            i = 0
            while True:
                name, value, _ = winreg.EnumValue(key, i)
                snapshot[f"{path}\\{name}"] = {
                    "value": value,
                    "hash": hash_value(value)
                }
                i += 1
        except OSError:
            pass

    return snapshot

def save_baseline(snapshot):
    with open(BASELINE_FILE, "w") as f:
        json.dump(snapshot, f, indent=4)

def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return {}
    with open(BASELINE_FILE, "r") as f:
        return json.load(f)