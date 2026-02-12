# 🔎 Web Recon CLI Tool

A Python-based Active Web Reconnaissance CLI tool that performs basic HTTP analysis, header inspection, redirect tracking, and security header evaluation.

This tool is designed for learning and demonstrating foundational web security and reconnaissance concepts.

---

## 🚀 Features

- 🌐 Send HTTP/HTTPS requests to target
- 📊 Display HTTP status code
- 📄 View full HTML response
- 📏 Show content length
- 🔐 Detect HTTPS usage
- 🖥 Display server information
- 📑 List full response headers
- 🛡 Analyze important security headers:
  - X-Frame-Options
  - Content-Security-Policy
  - Strict-Transport-Security
  - X-Content-Type-Options
- 🔁 Detect redirect chains
- 💾 Save selected outputs to a report file

---

## 🧠 What This Project Demonstrates

- Understanding of HTTP protocol
- Active reconnaissance concepts
- HTTP status code interpretation
- Security header analysis
- Redirect behavior analysis
- Modular function design in Python
- File handling and CLI interaction

---

## 🛠 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Arpitmeh-glitch/web-recon-cli.git
cd web-recon-cli

2️⃣ Install dependencies
pip install requests

▶ Usage
Run the tool using:
python main.py
(Enter a target domain when prompted:)
Enter the url: example.com
(Then choose options from the interactive menu.)
📂 Example Capabilities
🔐 Security Header Analysis

Checks for common security configuration headers and reports whether they are present or missing.

🔁 Redirect Detection

Displays full redirect chain including:

Intermediate status codes

Final destination URL

## 📸 Screenshots

### 🔹 Tool Usage Example 1
![Tool Usage 1](assets/Output_Usage1.png)

### 🔹 Tool Usage Example 2
![Tool Usage 2](assets/Output_Usage2.png)

### 🔹 Report File Output
![Report File](assets/ReportFile.png)

⚠️ Disclaimer

This tool is intended for educational purposes only.

Only use this tool on:

Websites you own

Systems you have permission to test

Unauthorized scanning or reconnaissance may violate laws or terms of service.

📌 Future Improvements

Port scanning module integration

Status code interpretation logic

Basic WAF/block detection

Modular file structure

Argument parsing (argparse)

Logging support

 

