SUSPICIOUS_KEYWORDS = [
    "powershell",
    "cmd.exe",
    "wscript",
    "cscript",
    "temp",
    "appdata",
    "disable",
]

DEFENDER_DISABLE_KEYS = [
    "DisableAntiSpyware",
    "DisableRealtimeMonitoring"
]

def analyze_change(key_path, new_value):
    findings = []

    value_str = str(new_value).lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in value_str:
            findings.append(
                ("HIGH", "Suspicious executable path detected")
            )

    for defender_key in DEFENDER_DISABLE_KEYS:
        if defender_key.lower() in key_path.lower():
            findings.append(
                ("CRITICAL", "Windows Defender tampering detected")
            )

    return findings
