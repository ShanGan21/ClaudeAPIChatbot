# Claude API Chatbot

A simple command-line chatbot built with the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python). It keeps the conversation history, so Claude remembers earlier messages in the same session.

## Requirements

- Python 3.9+
- An Anthropic API key from https://console.anthropic.com/settings/keys

## Setup

1. Create and activate a virtual environment:

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```
   pip install anthropic python-dotenv
   ```

3. Create a `.env` file in the project folder with your API key:

   ```
   ANTHROPIC_API_KEY=your-key-here
   ```

   The `.env` file is listed in `.gitignore`, so it won't be committed. Never share your key or commit it to GitHub.

## Usage

```
python chatbot.py
```

Type your message at the `You:` prompt. Type `exit` to quit.

## Project structure

```
chatbot.py   # the chatbot
.env         # your API key (not committed)
.gitignore   # files excluded from git
```
