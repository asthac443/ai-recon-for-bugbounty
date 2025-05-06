# 🧠 AI Recon for Bug Bounty  
**LLMs in the Loop: AI-Driven Recon for Modern Bug Hunters**

> This project demonstrates how AI and automation can supercharge passive reconnaissance for bug bounty hunting. It features a modular pipeline that uses LLMs (Large Language Models), public OSINT sources, and Python scripting to identify attack surfaces smarter and faster.

---

## 📌 Project Objective
Traditional recon tools often miss hidden gems buried in public data. This project integrates AI into the recon loop to:
- Discover subdomains and endpoints from public sources
- Extract secrets or API keys from GitHub
- Infer technology stacks and attack surface
- Correlate scattered recon data using LLMs

---

## 🧩 Modules Overview

| Module | Description |
|--------|-------------|
| `github_scraper.py` | Scrapes GitHub repos for keywords, secrets, endpoints |
| `subdomain_finder.py` | Gathers subdomains using passive OSINT |
| `tech_stack_detector.py` | Infers web tech stack from headers/content |
| `ai_keyword_extractor.py` | Uses OpenAI API to extract contextually important info |
| `recon_pipeline.py` | Main orchestration script tying modules together |

---

## ⚙️ Setup

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-recon-for-bugbounty.git
cd ai-recon-for-bugbounty
```

### 2. Install Dependencies
Create a virtual environment and install requirements:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
>⚠️ If requirements.txt not yet added, you can manually install:

```bash
pip install requests openai beautifulsoup4
```
### 3. Configure OpenAI API
Set your API key as an environment variable:
```bash
export OPENAI_API_KEY="sk-..."
```




# 🚀 Usage
Run the main pipeline:
```bash
python recon_pipeline.py --target yourdomain.com
```
Expected Output:

* Subdomains listed

* GitHub endpoints extracted

* Stack guessed (Apache, React, etc.)

* AI-extracted insights (e.g. hidden endpoints, secret patterns)




# 📊 Sample Output
```css
[*] Found 12 subdomains via OSINT
[*] Scraped 4 public GitHub repos
[*] Extracted 3 suspicious tokens via AI
[*] Likely tech stack: Flask + Nginx + PostgreSQL
```




# 📂 Project Structure
```kotlin
ai-recon-for-bugbounty/
├── recon_pipeline.py
├── modules/
│   ├── github_scraper.py
│   ├── subdomain_finder.py
│   ├── tech_stack_detector.py
│   └── ai_keyword_extractor.py
├── data/
│   └── sample_outputs/
├── notebooks/
│   └── LLM_analysis_demo.ipynb
└── README.md
```




# 📎 References
* [OpenAI API Docs](https://platform.openai.com/docs/overview)

* [GitHub Dorking Cheatsheet](https://github.com/techgaun/github-dorks)

* [Recon-ng](https://github.com/lanmaster53/recon-ng)

* [OWASP Top 10](https://owasp.org/www-project-top-ten/)





# 👨‍💻 Author
Aditya Shankar Tripathi

Senior Cybersecurity Professional | AI Security Enthusiast | Bug Bounty Hunter

GitHub: @asthac443

[LinkedIn](https://www.linkedin.com/in/aditya-shankar-2552bba5/)





# ⭐ Star the Repo
If this project helps you level up your recon — give it a ⭐️ on GitHub!


