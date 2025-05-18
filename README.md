# 🛡️ VulnPro-Python-Project

## 🔍 VulnPro — Advanced Vulnerability Scanner for Web Targets

**VulnPro** is a Python-based, CLI-powered vulnerability scanner built for **ethical hackers**, **penetration testers**, and **bug bounty hunters**.  
It automates web scanning, fuzzing, and reporting using custom payloads — fast, flexible, and powerful.

---

## ⚔️ Features

- 🎯 Scan single or multiple targets
- 🧪 Payload-based fuzzing engine
- 🎭 Random User-Agent + optional proxy rotation
- 🧵 Multi-threaded requests
- 💾 Export results to a file
- 🖼️ Dynamic ASCII banner per scan
- 🔁 Smart timeout + retry logic
- 🌈 Colorized CLI output using `colorama`

---

## ⚙️ Requirements

- Python >= 3.6
- `requests`
- `colorama`

> 📦 Install dependencies:
```bash
pip install -r requirements.txt

🚀 Usage Examples
🔗 Scan a single target

vulnpro -u https://example.com -p payloads.txt

📜 Scan multiple targets from a file

vulnpro -l urls.txt -p payloads.txt

⚡ Enable fast scan + verbose output

vulnpro -u https://target.com -p payloads.txt -f -v

💾 Save results to a file

vulnpro -u https://target.com -p payloads.txt -o results.txt

🛠️ Command-Line Options
Flag	Description
-u	Scan a single URL
-l	Load multiple URLs from file
-p	Path to payloads file (required)
-f	Fast mode (scan with top 5 payloads)
-v	Verbose output
-t	Threads to use (default: 5)
--timeout	Request timeout in seconds (default: 30)
--retries	Retry count if timeout occurs (default: 3)
--proxy	Enable random proxy usage
-o	Output file for results

📄 License
This project is licensed under the MIT License.

👾 Stay Legal
This tool is intended only for authorized testing and educational purposes.
Use responsibly — you're accountable for your actions.
