# VulnPro-Python-Project
# 🔍 VulnPro - Advanced Vulnerability Scanner

**VulnPro** is a powerful Python-based vulnerability scanner designed for ethical hackers, penetration testers, and bug bounty hunters. It automates scanning, fuzzing, and reporting of web vulnerabilities using user-supplied payloads.

---

## 🚀 Features

- 🎯 Scan single or multiple URLs
- 🧪 Payload-based fuzzing
- 🎭 Random User-Agent + optional proxy support
- 🧵 Multi-threaded execution
- 📁 Save output to a file
- 🖼️ ASCII banner with each scan
- 🔁 Timeout/retry logic
- 🎨 Colored output using `colorama`

---

## ⚙️ Requirements

- Python 3.6+
- `requests`
- `colorama`

### Install dependencies:
---

## 🚀 Usage

### Scan a single URL:

```bash
vulnpro -u https://example.com -p payloads.txt

```bash
pip install -r requirements.txt

### Scan a multiple URL:
vulnpro -l urls.txt -p payloads.txt

### Enable fast mode with verbose output:
vulnpro -u https://target.com -p payloads.txt -f -v

### Save results to a file:
vulnpro -u https://target.com -p payloads.txt -o results.txt


---

### ✅ **Command-Line Options**

You can also add this under the usage examples:

```md
---

## ⚙️ Options

| Flag         | Description                              |
|--------------|------------------------------------------|
| `-u`         | Single URL to scan                       |
| `-l`         | File containing list of URLs             |
| `-p`         | Payloads file path (required)            |
| `-f`         | Fast scan (only first 5 payloads)        |
| `-v`         | Verbose mode                             |
| `-t`         | Number of threads (default: 5)           |
| `--timeout`  | Request timeout in seconds (default: 30) |
| `--retries`  | Retry attempts if timeout (default: 3)   |
| `--proxy`    | Enable random proxy for each request     |
| `-o`         | Output file to save results              |


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).




