# 🤖 AI Commit Summary Agent

This tool uses a free LLM API from [Groq](https://groq.com/) to automatically generate meaningful Git commit messages based on your staged code changes (`git diff`). It follows the **Conventional Commits** format and provides a short reasoning for each change.

---

## 🚀 Features

- AI-generated commit messages based on `git diff`
- Explains the purpose of each commit
- CLI- and Git-hook-friendly
- Integrates with VSCode tasks

---

## 🛠 Requirements

- Python 3.7+
- Groq API key ([Get one free here](https://console.groq.com/))
- `requests` Python package:
  ```bash
  pip install requests
  ```

You can add a custom task in .vscode/tasks.json:

{
"label": "AI Commit Summary",
"type": "shell",
"command": "python replace-this-with-the-script-path"
}

Then run via Command Palette → Run Task → AI Commit Summary.
