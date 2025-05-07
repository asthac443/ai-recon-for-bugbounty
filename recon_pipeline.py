# Main orchestration script for recon pipeline
import os
import subprocess
import sys

def run_subdomain_finder(domain):
    print("[1/4] 🔍 Running Subdomain Finder...")
    subprocess.run(["python", "subdomain_finder.py", domain], check=True)

def run_github_scraper(domain):
    print("[2/4] 🛠️  Running GitHub Scraper...")
    subprocess.run(["python", "github_scraper.py", domain], check=True)

def run_tech_stack_detector():
    print("[3/4] 🧪 Running Tech Stack Detector...")
    subprocess.run(["python", "tech_stack_detector.py"], check=True)

def run_ai_keyword_extractor():
    print("[4/4] 🤖 Running AI Keyword Extractor...")
    subprocess.run(["python", "ai_keyword_extractor.py", "output/github_leaks.txt"], check=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python recon_pipeline.py <target_domain>")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"🚀 Starting AI-Powered Recon for: {domain}\n")

    run_subdomain_finder(domain)
    run_github_scraper(domain)
    run_tech_stack_detector()
    run_ai_keyword_extractor()

    print("\n✅ Recon Complete! Check the 'output/' folder for results.")

if __name__ == "__main__":
    main()
