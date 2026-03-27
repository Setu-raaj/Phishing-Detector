# Phishing-Detector
Phish-Detector is a web-based phishing URL detection tool built with Python and Flask. It analyzes URLs in real-time and flags suspicious patterns like IP addresses, fake domains, missing HTTPS, and more. It returns a color-coded threat verdict — Safe, Suspicious, or Phishing — with a detailed risk score.

A web-based phishing URL detection tool built with **Python** and **Flask**. It analyzes URLs in real-time and flags suspicious patterns commonly used in phishing attacks.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

---

## 📖 About the Project

Phishing is one of the most common cyberattacks where attackers trick users into visiting fake websites to steal sensitive information like passwords and credit card numbers.

**PhishGuard** is a beginner-friendly cyber security project that detects phishing URLs by analyzing suspicious patterns such as:
- Use of IP addresses instead of domain names
- Suspicious domain extensions
- Presence of `@` symbols
- Lack of HTTPS
- Unusually long URLs
- Excessive subdomains

---

## ✨ Features

- 🔍 **Real-time URL scanning** via a clean web interface
- 🟢🟡🔴 **Color-coded threat verdict** — Safe / Suspicious / Likely Phishing
- 📊 **Threat score bar** showing risk level
- ⚠️ **Detailed flag list** explaining what triggered the alert
- 🕓 **Recent scan history** — last 5 scans stored in the session
- ⌨️ **Keyboard support** — press Enter to scan instantly
- 🌐 **REST API** — can be tested with tools like Postman or curl

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Python 3.12, Flask      |
| Frontend  | HTML, CSS, JavaScript   |
| URL Parsing | `urllib`, `tldextract` |
| HTTP Requests | `requests`          |
| Styling   | Custom CSS (Dark Cyberpunk Theme) |

---

## 📁 Project Structure

```
phishing-detector/
├── app.py                  # Flask backend & URL analysis logic
└── templates/
    └── index.html          # Frontend UI
```

---

## ⚙️ Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

Or simply create the folder manually and add `app.py` and `templates/index.html`.

### 2. Install Required Libraries

```bash
python -m pip install flask requests tldextract
```

---

## ▶️ How to Run

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## ⚙️ How It Works

### URL Analysis Logic (`app.py`)

The tool extracts the following features from a URL and checks for red flags:

| Check | Suspicious Indicator |
|-------|----------------------|
| URL Length | Greater than 75 characters |
| IP Address | Numeric IP used instead of domain name |
| @ Symbol | Presence of `@` in the URL |
| Domain Extension | `.xyz`, `.tk`, `.pw`, `.top`, `.club` |
| HTTPS | URL does not use HTTPS |
| Subdomains | More than 2 levels of subdomains |

### Risk Score

| Score | Verdict |
|-------|---------|
| 0 | ✅ Looks Safe |
| 1–2 | ⚠️ Suspicious |
| 3+ | 🚨 Likely Phishing |

### API Endpoint

**POST** `/check`

Request body:
```json
{
  "url": "http://192.168.1.1/login/paypal"
}
```

Response:
```json
{
  "url": "http://192.168.1.1/login/paypal",
  "verdict": "🚨 Likely Phishing",
  "flags": [
    "Uses IP address instead of domain name",
    "Not using HTTPS"
  ],
  "risk_score": 2
}
```

---

## 🚀 Future Enhancements

- [ ] Integrate **Machine Learning** model (Random Forest / XGBoost) for smarter detection
- [ ] Add **Google Safe Browsing API** for real-time blacklist checking
- [ ] Add **WHOIS lookup** to check domain age
- [ ] Build a **Browser Extension** for automatic phishing warnings
- [ ] Add **email scanner** to detect phishing links in emails
- [ ] Deploy to cloud (Render / Railway / Heroku)

---

## 👨‍💻 Author

Built as a **Cyber Security Academic Project**

> ⚠️ **Disclaimer:** This tool is built for educational purposes only. It is not a substitute for professional security software.
