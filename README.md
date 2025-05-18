# 🔍 VulnPro - Advanced Vulnerability Scanner

Quickly identify potential web vulnerabilities using customizable payloads and threaded scanning.

---

## 🚀 Features

* ✅ Custom payload injection
* ✅ Multi-threaded scanning
* ✅ Proxy support
* ✅ Timeout and retry handling
* ✅ Fast mode (for quick testing)
* ✅ Saves results to file
* ✅ Cool banner + colorized output

---

## ⚙️ Usage

### 🔗 Scan a single URL:

```bash
python vulnpro.py -u http://example.com -p payloads.txt
```

### 🔄 Scan multiple URLs:

```bash
python vulnpro.py -l urls.txt -p payloads.txt
```

### ⚡ Fast mode (checks only first 5 payloads):

```bash
python vulnpro.py -u http://example.com -p payloads.txt -f
```

### 🧪 Verbose output:

```bash
python vulnpro.py -u http://example.com -p payloads.txt -v
```

### 🌐 Use proxy + timeout + retry:

```bash
python vulnpro.py -u http://example.com -p payloads.txt --proxy --timeout 20 --retries 2
```

### 💾 Save results to file:

```bash
python vulnpro.py -u http://example.com -p payloads.txt -o results.txt
```

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Content of `requirements.txt`:

```text
requests
colorama
```

---

## 📁 File Structure

```
├── vulnpro.py
├── requirements.txt
├── payloads.txt
├── urls.txt
└── README.md
```

---

## 🙋‍♂️ Author

**ABHI 🚀**
[Telegram: @Aaloo\_bhujiaa](https://t.me/Aaloo_bhujiaa)

---

## 📜 License

This project is licensed under the [**GNU GPL v3.0**](LICENSE).
