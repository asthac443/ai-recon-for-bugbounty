# Module to extract relevant data using LLMs
import openai
import os
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_keywords(text):
    prompt = f"""
You are a cybersecurity analyst helping with bug bounty reconnaissance.
Extract the most relevant keywords, technologies, domains, parameters, and suspicious patterns from the following input:

{text}

Return the result as a bullet list.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for bug bounty recon."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )
        result = response.choices[0].message.content.strip()
        return result
    except Exception as e:
        print("[-] OpenAI API error:", str(e))
        return "Error: Could not generate keywords."

def main(input_file):
    if not os.path.exists(input_file):
        print("[-] Input file not found.")
        return

    with open(input_file, "r") as f:
        data = f.read()

    print("[+] Extracting keywords using LLM...")
    keywords = extract_keywords(data)

    os.makedirs("output", exist_ok=True)
    with open("output/ai_keywords.txt", "w") as f:
        f.write(keywords)

    print("[+] Done. Keywords saved to output/ai_keywords.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ai_keyword_extractor.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
