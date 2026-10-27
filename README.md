# MailMind AI

**Draft email replies with the help of your tone choice and relevant examples.**

[![GitHub](https://img.shields.io/badge/GitHub-Source-24292f?logo=github)](https://github.com/chyk2468/MailMind-AI)

## 1. Project Title & Tagline

Draft email replies with the help of your tone choice and relevant examples.

## 2. Problem Statement

Writing a reply that fits the message and the intended tone takes time. MailMind retrieves similar examples and uses them as context for a generated draft.

## 3. Project Preview

![MailMind AI screenshot](../Working%20Screenshot.png)

[Interactive architecture explorer](architecture.html)

## 4. Overview

The Streamlit interface accepts a message and tone, the RAG engine retrieves related examples from a local ChromaDB collection, and the generator creates a draft with Gemini. The user reviews the result before sending.

## 5. Key Features

- Email or message input with tone selection.
- Local semantic retrieval from sample emails.
- Gemini-generated reply drafts grounded in retrieved examples.
- Copy or download the generated text.

## 6. Architecture / Workflow

![Animated MailMind AI workflow](readme-architecture.svg)

The diagram animates the flow between stages. Open the [interactive architecture explorer](architecture.html) to select each stage and read its role.

## 7. Tech Stack

Python, Streamlit, Sentence Transformers, ChromaDB, Google Gemini

## 8. Installation & Setup

```bash
git clone https://github.com/chyk2468/MailMind-AI.git
cd MailMind-AI
python -m venv .venv
pip install -r requirements.txt
```

## 9. Usage

1. Configure the Gemini API key using the environment variable expected by the app.
2. Start the interface with `streamlit run app.py`.
3. Enter an email, choose a tone, and generate a draft.
4. Check the result before copying it into your email client.

## 10. Project Structure

- `app.py`: Streamlit interface
- `rag_engine.py`: retrieval and context preparation
- `ai_generator.py`: Gemini reply generation
- `sample_data/`: example messages
- `requirements.txt`: Python dependencies

## 11. Results & Demo

The repository includes `Working Screenshot.png`. Use it as the current visual reference. Add a short GIF of the message-to-draft flow when a fresh recording is available.

## 12. Future Enhancements

- Add tests for retrieval quality and tone consistency.
- Add support for user-managed example collections.
- Show retrieved context sources beside each draft.
- Add configurable privacy and retention controls.

## 13. License

Check the repository for a `LICENSE` file. If absent, add a license before granting reuse or redistribution rights.
