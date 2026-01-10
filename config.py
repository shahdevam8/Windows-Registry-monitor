import winreg

REGISTRY_KEYS = [
    (winreg.HKEY_CURRENT_USER,
     r"Software\Microsoft\Windows\CurrentVersion\Run"),

    (winreg.HKEY_LOCAL_MACHINE,
     r"Software\Microsoft\Windows\CurrentVersion\Run"),

    (winreg.HKEY_LOCAL_MACHINE,
     r"Software\Policies\Microsoft\Windows Defender"),

    (winreg.HKEY_LOCAL_MACHINE,
     r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
]

SUSPICIOUS_PATHS = ["AppData", "Temp", "Public"]