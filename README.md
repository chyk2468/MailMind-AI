<div align="center">

# 📩 MailMind AI

### RAG-Powered Smart Email Reply Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-RAG-7c3aed?style=for-the-badge)](https://trychroma.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

> **MailMind AI** is a next-generation, AI-powered email reply generator that combines  
> **Retrieval-Augmented Generation (RAG)** with **Google Gemini 2.0 Flash** to produce  
> smarter, context-aware replies with your choice of tone — in seconds.

</div>

---

## ✨ What's New — RAG Edition

| Feature | Details |
|---|---|
| 🧠 **RAG Engine** | Retrieves semantically similar past emails via ChromaDB before generating |
| 📚 **Knowledge Base** | 15 curated seed emails pre-loaded; upload your own via the sidebar |
| ⚡ **Richer Replies** | Gemini prompt is enriched with real context for more accurate responses |
| 🎨 **New UI** | Gradient dark UI, Inter font, live RAG badge, responsive sidebar |

---

## 🌟 Key Features

- 🎯 **Smart Tone Selection** — 8 emotionally aware tones: Formal, Friendly, Apologetic, Professional, Appreciative, Assertive, Sympathetic, Informative
- 🔍 **RAG-Powered Context** — retrieves top-3 semantically similar emails and injects them into the Gemini prompt
- 📚 **Expandable Knowledge Base** — upload your own `.txt` emails through the sidebar to personalise responses
- 💡 **Gemini 2.0 Flash** — fast, accurate, and context-aware generation
- 📋 **Copy to Clipboard** — one-click with animated confirmation
- 📥 **Download as .txt** — save replies instantly
- 🖥️ **Responsive Dark UI** — works beautifully on desktop and mobile

---

## 🏗️ Architecture

```
User Email Input
      │
      ▼
┌─────────────────────────┐
│   sentence-transformers  │   ← embeds the email (all-MiniLM-L6-v2)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       ChromaDB           │   ← vector similarity search (cosine)
│   (Local Persistent DB)  │   ← returns top-3 similar emails
└────────────┬────────────┘
             │  RAG Context
             ▼
┌─────────────────────────┐
│   Gemini 2.0 Flash API   │   ← enriched prompt = email + context + tone
└────────────┬────────────┘
             │
             ▼
      AI-Generated Reply
```

---

## 📁 Project Structure

```
MailMind-AI/
│
├── app.py                   # Streamlit frontend + RAG integration
├── ai_generator.py          # Gemini prompt builder + reply generator
├── rag_engine.py            # ChromaDB vector store + retrieval engine
│
├── sample_data/
│   └── sample_emails.py     # 15 seed emails for all 8 tones
│
├── .chroma_db/              # Auto-created persistent vector store
├── .env                     # Your API key (not committed)
├── .env.example             # Template for .env
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | [Streamlit](https://streamlit.io/) + Custom CSS |
| **LLM** | [Google Gemini 2.0 Flash](https://ai.google.dev/) |
| **Vector Store** | [ChromaDB](https://trychroma.com/) (local persistent) |
| **Embeddings** | [sentence-transformers](https://sbert.net/) (`all-MiniLM-L6-v2`) |
| **RAG Retrieval** | Cosine similarity, top-k nearest neighbour |

---

## 🧠 How It Works

```
1. App starts  →  15 seed emails are embedded & stored in ChromaDB (first run)
2. User pastes email  →  email is embedded using sentence-transformers
3. ChromaDB retrieves  →  top-3 most semantically similar emails from the KB
4. Prompt is built  →  [tone instruction] + [retrieved context] + [user email]
5. Gemini generates  →  a tone-specific, context-aware reply
6. User can copy/download  →  ready-to-send reply in seconds
```

---

## 📸 Screenshots

**Step 1 — Interface**
![Interface Screenshot](https://github.com/user-attachments/assets/4cec8aca-c203-4c68-9940-7a0fd513b19a)

**Step 2 — Paste Email & Generate**
![Generate Reply](https://github.com/user-attachments/assets/75f45176-3624-4c07-b0be-6a4cd35eb1cb)

**Step 3 — RAG-Enhanced Reply**
![AI Reply](https://github.com/user-attachments/assets/2fb3fccf-83d1-44af-ae7d-a584b6e35594)

---

## 🧪 Example

### ✉️ Input Email:
```
Hi Priya,

Thanks for today's discussion. Can you send over
the revised project timeline by tomorrow?

Regards,
Sanjay
```

### 🎯 Tone: Appreciative · RAG context retrieved: 3 similar emails

### 🤖 Generated Reply:
```
Hi Sanjay,

Thank you for the engaging discussion today — I truly appreciate
your clarity and valuable insights.

I'll ensure the updated project timeline reaches you by tomorrow
morning. Please feel free to reach out if you need anything else.

Best regards,
Priya
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/CH-Yashwant-Kumar/MailMind-AI.git
cd MailMind-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ `sentence-transformers` will download the `all-MiniLM-L6-v2` model (~90 MB) on first run.

### 3. Set Your Google API Key

Copy the example env file and add your key:

```bash
cp .env.example .env
```

Edit `.env`:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get your free key at [aistudio.google.com](https://aistudio.google.com/app/apikey).

### 4. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.  
On first run, the knowledge base is seeded automatically with 15 example emails.

---

## 📚 Using the Knowledge Base

1. Open the **📚 Knowledge Base** sidebar panel
2. Click **Browse files** to upload `.txt` email files
3. Select the appropriate tone label
4. Click **📥 Add to Knowledge Base**
5. The KB counter updates and future replies use your uploaded emails as context

---

## 🔐 Security Notes

- **Never** commit your `.env` file or expose your API key
- `.env` is listed in `.gitignore`
- Use environment variables in production deployments

---

## 📦 Requirements

```
streamlit
google-generativeai
python-dotenv
chromadb
sentence-transformers
```

---

## 👨‍💻 Author

<div align="center">

Made with ❤️ by **Ch. Yashwant Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-CH--Yashwant--Kumar-181717?style=flat-square&logo=github)](https://github.com/CH-Yashwant-Kumar)

</div>

---

<div align="center">

Enjoy the ✨ power of **RAG-enhanced** AI communication with **MailMind AI**!

</div>
