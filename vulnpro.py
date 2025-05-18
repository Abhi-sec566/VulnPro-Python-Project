# vulnpro.py
import requests
import argparse
import threading
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Color auto reset

# Random User-Agents list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 11)"
]

# Proxy support (Optional, add your proxies)
proxies_list = [
    # "http://127.0.0.1:8080",
    # "http://your.proxy:port",
]

def check_vulnerabilities(url, payloads, verbose=False, timeout_value=30, retries=3, proxy_enabled=False):
    vulnerabilities_found = []

    for payload in payloads:
        target_url = url + payload
        headers = {
            "User-Agent": random.choice(user_agents)
        }
        proxy = {"http": random.choice(proxies_list), "https": random.choice(proxies_list)} if proxy_enabled and proxies_list else None

        for attempt in range(retries):
            try:
                response = requests.get(target_url, headers=headers, timeout=timeout_value, proxies=proxy)
                if payload in response.text:
                    vulnerabilities_found.append(payload)
                    print(Fore.GREEN + f"[+] Vulnerability found with payload: {payload}")
                    break
                elif verbose:
                    print(Fore.YELLOW + f"[-] Checked payload: {payload} - No vulnerability.")
                break
            except requests.exceptions.ReadTimeout:
                print(Fore.RED + f"[!] Timeout on {payload} (Attempt {attempt+1}/{retries})")
                time.sleep(2)
            except Exception as e:
                print(Fore.RED + f"[!] Error: {e}")
                break

    return vulnerabilities_found

def load_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return list(set([line.strip() for line in f if line.strip()]))
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        return []

def scan_url(url, payloads, fast, verbose, timeout_value, retries, proxy_enabled, save_file):
    print(Fore.CYAN + f"\n[~] Scanning {url} ...")
    payloads_to_check = payloads[:5] if fast else payloads

    found = check_vulnerabilities(url, payloads_to_check, verbose, timeout_value, retries, proxy_enabled)

    if found:
        print(Fore.GREEN + f"\n[+] Vulnerabilities found on {url}:")
        for vuln in found:
            print(Fore.GREEN + f"- {vuln}")
        if save_file:
            try:
                with open(save_file, 'a') as f:
                    f.write(f"\n[+] {url}\n")
                    for vuln in found:
                        f.write(f" - {vuln}\n")
            except Exception as e:
                print(Fore.RED + f"[!] Could not write to file {save_file}: {e}")
    else:
        print(Fore.RED + f"\n[-] No vulnerabilities found on {url}.")

def banner():
    colors = [
        Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
        Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX,
        Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW
    ]
    logos = [
        r"""
 __     __     _       ____            
\ \   / /   _| |_ __ |  _ \ _ __ ___  
 \ \ / / | | | | '_ \| |_) | '__/ _ \ 
  \ V /| |_| | | | | |  __/| | | (_) |
   \_/  \__,_|_|_| |_|_|   |_|  \___/ 
""",
        r"""
 __   __           _       _             
 \ \ / /          | |     | |            
  \ V /___  _   _ | |_ ___| |_ ___  _ __ 
   \ // _ \| | | || __/ _ \ __/ _ \| '__|
   | | (_) | |_| || ||  __/ || (_) | |   
   \_/\___/ \__,_| \__\___|\__\___/|_|   
""",
        r"""
 __      __      _   _   _   _   _   _  
/ _\    /__\    /_\ | | | | | | | | | | 
\ \    /_\     //_\\| |_| |_| |_| |_| | 
_\ \  //__   /  _  \  _  _  _  _  _  | 
\__/  \__/   \_/ \_/_| |_| |_| |_| |_| 
""",
        r"""
 __      ___      _   _   _   _   _   _  
 \ \    / (_)    | | | | | | | | | | | | 
  \ \  / / _  ___| |_| |_| |_| |_| |_| | 
   \ \/ / | |/ __| __| __| __| __| __| | 
    \  /  | | (__| |_| |_| |_| |_| |_| | 
     \/   |_|\___|\__|\__|\__|\__|\__|_| 
""",
        r"""
 ____   _   _   _   _   _   _   _   _  
|  _ \ | | | | | | | | | | | | | | | | 
| |_) || |_| |_| |_| |_| |_| |_| |_| | 
|  __/  \__,_|\__,_|\__,_|\__,_|\__,_| 
|_|                                    
"""
    ]
    logo_color = random.choice(colors)
    logo = random.choice(logos)
    print(logo_color + logo)
    print(logo_color + "   Advanced Vulnerability Scanner")
    print(logo_color + "   Created by: ABHI 🚀 (Telegram: @Aaloo_bhujiaa)\n")

def main():
    banner()

    parser = argparse.ArgumentParser(description="Advanced Vulnerability Scanner by ABHI 🚀")
    parser.add_argument('-u', '--url', help='Specify a single URL to scan.')
    parser.add_argument('-l', '--list', help='Specify a file containing list of URLs.')
    parser.add_argument('-p', '--payload', required=True, help='Path to payloads file.')
    parser.add_argument('-t', '--threads', type=int, default=5, help='Number of threads to use.')
    parser.add_argument('-f', '--fast', action='store_true', help='Fast scan (first 5 payloads).')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode.')
    parser.add_argument('--timeout', type=int, default=30, help='Timeout per request (default=30s).')
    parser.add_argument('--retries', type=int, default=3, help='Retries if timeout occurs (default=3).')
    parser.add_argument('--proxy', action='store_true', help='Use random proxy for each request.')
    parser.add_argument('-o', '--output', help='Save results to a file.')

    args = parser.parse_args()

    payloads = load_file(args.payload)
    if not payloads:
        print(Fore.RED + "No payloads loaded. Exiting.")
        return

    urls = []
    if args.url:
        urls.append(args.url)
    elif args.list:
        urls = load_file(args.list)

    if not urls:
        print(Fore.RED + "No URLs to scan. Exiting.")
        return

    threads = []
    for url in urls:
        thread = threading.Thread(
            target=scan_url,
            name=f"Scanner-{url}",
            args=(url, payloads, args.fast, args.verbose, args.timeout, args.retries, args.proxy, args.output)
        )
        threads.append(thread)
        thread.start()

        # Limit active threads
        while threading.active_count() > args.threads:
            time.sleep(0.5)

    for thread in threads:
        thread.join()

    print(Fore.LIGHTGREEN_EX + "\n[✔] Scan completed. Thank you for using tool by ABHI 💥")

if __name__ == "__main__":
    main()
