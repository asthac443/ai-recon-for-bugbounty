# Module to detect tech stacks from headers/content
import requests
import sys
import os
from bs4 import BeautifulSoup

def detect_stack(url):
    stack_info = []

    try:
        response = requests.get(f"http://{url}", timeout=5)
    except Exception:
        try:
            response = requests.get(f"https://{url}", timeout=5, verify=False)
        except Exception:
            return "Unreachable"

    server = response.headers.get("Server")
    powered_by = response.headers.get("X-Powered-By")

    if server:
        stack_info.append(f"Server: {server}")
    if powered_by:
        stack_info.append(f"X-Powered-By: {powered_by}")

    # Try to fingerprint CMS/framework
    soup = BeautifulSoup(response.text, "html.parser")
    if "wp-content" in response.text:
        stack_info.append("CMS: WordPress")
    elif "react" in response.text.lower():
        stack_info.append("Framework: React")
    elif "angular" in response.text.lower():
        stack_info.append("Framework: Angular")

    return ", ".join(stack_info) if stack_info else "Unknown"

def main(subdomain_file):
    os.makedirs("output", exist_ok=True)
    
    try:
        with open(subdomain_file, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[-] Subdomain file not found.")
        return

    print("[+] Detecting tech stack for subdomains...")
    results = []

    for sub in subdomains:
        stack = detect_stack(sub)
        results.append(f"{sub} -> {stack}")
        print(f"  [>] {sub}: {stack}")

    with open("output/tech_stack.txt", "w") as f:
        f.write("\n".join(results))

    print("[+] Done. Results saved to output/tech_stack.txt")

if __name__ == "__main__":
    if not os.path.exists("output/subdomains.txt"):
        print("[-] Run subdomain_finder.py first.")
        sys.exit(1)

    main("output/subdomains.txt")
