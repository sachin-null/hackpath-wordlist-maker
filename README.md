# 📋 HackPath Wordlist Maker v2

> **6-in-1 Targeted wordlist generator for security professionals**
> Created by **Sachin Ser** | HackPath

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-2.0-green?style=flat-square)](https://github.com/sachin-null/hackpath-wordlist-maker)
[![Platform](https://img.shields.io/badge/Platform-Termux%20|%20Linux%20|%20Kali-orange?style=flat-square)](https://github.com/sachin-null)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![HackPath](https://img.shields.io/badge/HackPath-CEH%20v12-red?style=flat-square)](https://github.com/sachin-null/hackpath)

---

## ⚡ All 6 Tools

| # | Tool | Features |
|---|------|---------|
| 1 | 👤 **Full Wordlist** | Name · DOB · Phone · Pet · City · Keyword · Company |
| 2 | ⚡ **Quick Mode** | Name + Birthday + 1 extra word |
| 3 | 🔑 **Keyword Wordlist** | Multiple keywords + combinations |
| 4 | 📁 **Combine Wordlists** | Merge multiple files + deduplicate |
| 5 | 🔍 **Filter Wordlist** | Filter by length · charset · content |
| 6 | 📊 **Wordlist Stats** | Analyze wordlist file |

---

## 📌 What's New in v2?

- Keyword Wordlist tool (NEW)
- Combine Wordlists — merge files (NEW)
- Filter Wordlist by charset/length (NEW)
- Wordlist Statistics analyzer (NEW)
- Company/School field added
- More leet speak variants (l→1 added)
- More suffix/prefix combinations
- Name parts splitting (first3+last3)
- Better date combinations

---

## 📲 Install & Run

### Termux (Android)
```bash
pkg install python git -y
git clone https://github.com/sachin-null/hackpath-wordlist-maker
cd hackpath-wordlist-maker
python3 wlmaker.py
```

### Kali Linux / Linux
```bash
git clone https://github.com/sachin-null/hackpath-wordlist-maker
cd hackpath-wordlist-maker
python3 wlmaker.py
```

### One Line (Termux)
```bash
pkg install python git -y && git clone https://github.com/sachin-null/hackpath-wordlist-maker && cd hackpath-wordlist-maker && python3 wlmaker.py
```

---

## 🖥️ Menu

```
  MENU
  [1] Full Wordlist      (all personal info)
  [2] Quick Mode         (name + birthday)
  [3] Keyword Wordlist   (multiple keywords)
  [4] Combine Wordlists  (merge files)
  [5] Filter Wordlist    (by length/charset)
  [6] Wordlist Stats     (analyze file)
  [0] Exit

  HackPath WL >
```

---

## 🎯 Birthday Format

```
Format  : ddmmyyyy
Example : 06062001  (June 6, 2001)

Generates variants like:
  06062001
  06062001!
  2001!
  0606
  200106
  06062001@
  ... and more
```

---

## 🔤 Mutations Generated

```
sachin       → original
SACHIN       → uppercase
Sachin       → capitalize
s@ch1n       → leet speak
S@ch1n       → leet capitalize
nihcas       → reversed
sachin123    → common suffix
Sachin@2024  → suffix combo
sachin_786   → underscore
mysachin     → prefix
sachin!      → special suffix
... 50+ variants per word
```

---

## 📊 Stats Output

```
  WORDLIST STATISTICS

  Total words        : 5,234
  Unique words       : 5,234
  Min length         : 4
  Max length         : 20
  Avg length         : 11.3
  File size          : 48.2 KB

  CHARSET ANALYSIS
  With uppercase     : 1,203 (23%)
  With lowercase     : 4,892 (93%)
  With digits        : 3,421 (65%)
  With special       : 1,876 (35%)
```

---

## 🔍 Filter Options

```
Min/Max length
Must have uppercase (Y/N)
Must have lowercase (Y/N)
Must have digit (Y/N)
Must have special char (Y/N)
Must contain specific string
```

---

## 📦 Requirements

```
Python 3.x only
Zero extra packages
Works offline
Termux / Kali / Ubuntu / Windows
```

---

## 🔄 Changelog

### v2.0
- 6 tools (was 2)
- Keyword Wordlist (new)
- Combine Wordlists (new)
- Filter Wordlist (new)
- Wordlist Stats (new)
- More leet variants
- Company field
- Better name splitting

### v1.0
- Full wordlist
- Quick mode

---

## ⚠️ Disclaimer

> For **authorized / educational use only**.
> Use only on systems you own or have permission to test.
> The author is not responsible for any misuse.

---

## 👤 Created by

**Sachin Ser** | [HackPath](https://github.com/sachin-null)

- GitHub: [@sachin-null](https://github.com/sachin-null)
- Instagram: [@sachin_ser](https://www.instagram.com/_sachin_ser_90?igsh=MWg2eTQxcTZhaGRkeA==)

---

## 🔗 More HackPath Tools

| Tool | Repo |
|------|------|
| 🔓 CTF Helper v2 | [hackpath-ctf-helper](https://github.com/sachin-null/hackpath-ctf-helper) |
| 🔐 PassGen v2 | [hackpath-passgen](https://github.com/sachin-null/hackpath-passgen) |
| 🌐 OSINT Tool | [hackpath-osint](https://github.com/sachin-null/hackpath-osint) |
| 📱 Phone Analyzer | [hackpath-phone-analyzer](https://github.com/sachin-null/hackpath-phone-analyzer) |

---

<div align="center">

**Star this repo if it helped you!**

`Made with love by Sachin Ser | HackPath`

</div>
