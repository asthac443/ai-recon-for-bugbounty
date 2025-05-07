# Module to find subdomains using OSINT tools
# subdomain_finder.py

import requests
import json

def fetch_subdomains_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain in sub:
                    subdomains.add(sub.strip())
        return sorted(subdomains)
    except Exception as e:
        print(f"[!] Error fetching subdomains from crt.sh: {e}")
        return []

def save_output(subdomains, output_file="output/subdomains.txt"):
    try:
        with open(output_file, "w") as f:
            for sub in subdomains:
                f.write(sub + "\n")
        print(f"[+] Subdomains saved to {output_file}")
    except Exception as e:
        print(f"[!] Error saving subdomains: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Find subdomains using crt.sh")
    parser.add_argument("domain", help="Target domain, e.g., example.com")
    args = parser.parse_args()

    subs = fetch_subdomains_crtsh(args.domain)
    save_output(subs)
