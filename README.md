# 🛡️ File Integrity Monitoring System

A lightweight Python tool to **monitor file changes** using **SHA-256 hash comparisons**. This script helps detect any unauthorized modifications, additions, or deletions in files within a directory — ideal for basic cybersecurity checks and integrity audits.

---

## 🚀 Features
- ✅ Tracks file **modifications**, **deletions**, and **new additions**
- ✅ Uses **SHA-256 hashing** for secure comparison
- ✅ Simple CLI-based design – no extra tools needed
- ✅ Ideal for students, interns, or beginners in cybersecurity

---

## 🧰 How It Works

1. **Generate a Baseline**  
   Create an initial record of all file hashes in a selected folder.
   ```bash
   python create_baseline.py
   ```

2. **Monitor for Changes**  
   Compare current file states with the saved baseline.
   ```bash
   python monitor.py
   ```

> ⚠️ Update the `'/your/folder/path'` in both scripts to your target directory.

---

## 📂 File Structure
```
file-integrity-monitor/
├── create_baseline.py    # Script to save original file hashes
├── monitor.py            # Script to detect changes
└── baseline.json         # Generated after running create_baseline.py
```

---

## 📘 Use Cases
- Cybersecurity mini-projects
- System audit scripts
- Internship or academic portfolio
- Personal data protection tools

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
