# Python LLM Assistant Tools

This repository contains interactive Python assistant tools, the main feature is its  local AI. we use this AI to do repetitive simple tasks instead of depending on cloud LLMs.


## Projects

### 1. LinkedIn Post Rewriter (`linkedin_rewriter.py`)
An interactive CLI tool that connects to a local LLM server (like LM Studio) to rewrite any text input into a polished, professional LinkedIn post.
* **Auto-Save feature:** Successfully generated posts are automatically saved to the `text/` directory with a timestamp (e.g., `text/post_YYYYMMDD_HHMMSS.txt`).

### 2. Local Chatbot (`chat.py`)
A conversational assistant running locally using `litert-lm`.

---

## Libraries and Dependencies
The project uses the following libraries (tracked in [requirements.txt](file:///d:/python/requirements.txt)):
* **`openai`**: Python client to connect to local or remote OpenAI-compatible APIs (like LM Studio).
* **`python-dotenv`**: Loads environment configuration from a `.env` file to keep API keys and local URLs secure and out of version control.
* **`litert-lm`**: Lightweight runtime engine for running local models.

---

## Setup and Installation

### 1. Install Dependencies
Ensure you have your virtual environment active and run:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your settings:
   * `OPENAI_API_KEY`: API key for your LLM provider (default: `lm-studio`).
   * `OPENAI_BASE_URL`: Base URL of your local/remote server (default: `http://localhost:1234`).
   * `LLM_MODEL`: Model name to use.

*(Note: `.env` is listed in `.gitignore` to ensure your personal details are never pushed to GitHub).*

---

## Running the Tools

### Run the LinkedIn Post Rewriter:
```bash
python linkedin_rewriter.py
```

### Run the Local Chatbot:
```bash
python chat.py
```
