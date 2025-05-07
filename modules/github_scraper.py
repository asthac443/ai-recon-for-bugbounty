# Module to scrape public GitHub data for recon
import requests
import sys
import time
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Set your token as an env var to avoid hardcoding
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

SEARCH_KEYWORDS = ["password", "secret", "token", "api_key", "auth", "key"]

def search_github(domain, keyword):
    query = f"{keyword} {domain}"
    url = f"https://api.github.com/search/code?q={query}&per_page=10"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 403:
        print("[-] Rate limited. Try using a GitHub token.")
        return []
    
    if response.status_code != 200:
        print(f"[-] GitHub API Error: {response.status_code}")
        return []

    results = response.json().get("items", [])
    return [item['html_url'] for item in results]

def main(domain):
    os.makedirs("output", exist_ok=True)
    all_results = []

    print(f"[+] Searching GitHub for leaks related to: {domain}")
    for keyword in SEARCH_KEYWORDS:
        print(f"  [>] Keyword: {keyword}")
        links = search_github(domain, keyword)
        all_results.extend(links)
        time.sleep(2)  # Respect rate limits

    output_file = f"output/github_leaks.txt"
    with open(output_file, "w") as f:
        for url in all_results:
            f.write(url + "\n")

    print(f"[+] Found {len(all_results)} potential leak URLs. Saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_scraper.py example.com")
        sys.exit(1)
    
    domain = sys.argv[1]
    main(domain)
