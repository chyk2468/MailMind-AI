"""
ai_generator.py — AI reply generation for MailMind AI.

Uses Google Gemini 2.0 Flash, optionally enriched with RAG context
retrieved from the local ChromaDB knowledge base.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")  # set in .env or env var
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_reply(email_text: str, tone: str, rag_context: str = "") -> str:
    """
    Generate a tone-specific email reply using Gemini 2.0 Flash.

    Parameters
    ----------
    email_text  : str – the received email body
    tone        : str – desired reply tone (e.g. 'Formal', 'Friendly')
    rag_context : str – optional block of similar example emails from the RAG engine
    """
    context_block = ""
    if rag_context:
        context_block = (
            f"\n\nHere are some similar email examples to guide your style:\n"
            f"{rag_context}\n"
        )

    prompt = (
        f"You are an expert AI assistant specialised in writing professional, "
        f"context-aware email replies.\n"
        f"{context_block}\n"
        f"Received Email:\n\"\"\"\n{email_text}\n\"\"\"\n\n"
        f"Write a {tone.lower()} reply to the above email. "
        f"The reply must clearly reflect the '{tone}' tone. "
        f"Keep it concise, polite, and directly relevant to the email content. "
        f"Do not add placeholders — write a complete, ready-to-send reply."
    )

    response = model.generate_content(prompt)
    return response.text.strip()
