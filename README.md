# Windows Registry Change Monitoring System

## 📌 Project Overview
The **Windows Registry Change Monitoring System** is a defensive security project designed to monitor, detect, and report unauthorized or suspicious changes made to critical Windows Registry keys.  
Since malware often abuses registry locations for persistence, privilege escalation, and security bypass, this tool helps defenders identify such activity early.

This project is **educational, SOC-focused, and blue-team oriented**.

---

## 🎯 What This Project Helps With
- Detects **malware persistence techniques**
- Identifies **unauthorized startup entries**
- Monitors **security configuration tampering**
- Provides **registry integrity validation**
- Builds **practical SOC & IR experience**
- Helps students understand **Windows internals**

---

## 🧠 Key Capabilities
- Autorun registry key monitoring (Run / RunOnce)
- Malware-like registry behavior detection
- Baseline snapshot & integrity comparison
- Timestamped logging of registry changes
- Alert-style reporting for suspicious activity

---

## 📁 Recommended Folder Structure

```
Windows_Registry_Monitor/
│
├── monitor.py
├── baseline.json
├── registry_logs.txt
├── report.txt
├── requirements.txt
├── README.md
└── venv/
```

---

## 📦 requirements.txt

```
pywin32
```

---

## 🐍 Virtual Environment Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python monitor.py
```

---

## 📄 Output Files

| File | Purpose |
|----|----|
| baseline.json | Registry baseline |
| registry_logs.txt | Change logs |
| report.txt | Final report |

---

## 🎓 Learning Outcomes
- Windows Registry internals
- Malware persistence detection
- SOC-style monitoring & reporting

---

## 🛡️ Ethical Use
Use only on systems you own or are authorized to test.
