import os
import requests
import git
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(GROQ_API_KEY)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-70b-8192"


def get_git_diff():
    repo = git.Repo(".", search_parent_directories=True)
    diff = repo.git.diff("HEAD")
    return diff


def generate_commit_summary(diff_text):
    prompt = f"""
                You are an expert software engineer.

                Given the following git diff, generate a concise and meaningful commit message. Follow the Conventional Commits style (e.g., feat: add new login flow, fix: correct typo).

                Also, briefly explain why this change was made.

                Git Diff: {diff_text}

                Respond in this format:
                Commit Message: <your message>
                Reason: <brief explanation>

            """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 300,
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Error:", response.status_code, response.text)
        return None


if __name__ == "__main__":
    print("📄 Fetching git diff...")
    diff_text = get_git_diff()

    if not diff_text.strip():
        print("✅ No changes detected (git diff is empty).")
    else:
        print("🤖 Generating commit message using Groq API...")
        summary = generate_commit_summary(diff_text)
        if summary:
            print("\n📝 Suggested Commit Message:\n")
            print(summary)
