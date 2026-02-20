"""
sample_data/sample_emails.py — Seed data for MailMind AI's knowledge base.

Call `seed_knowledge_base()` once on app startup to pre-populate the ChromaDB
vector store with representative email examples for all 8 tones.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from rag_engine import add_email

SEED_EMAILS = [
    # ── Formal ──────────────────────────────────────────────────────────────
    {
        "tone": "Formal",
        "text": (
            "Dear Mr. Sharma,\n\n"
            "I am writing to formally acknowledge receipt of your proposal dated "
            "15th February 2025. We have reviewed the document with our internal "
            "stakeholders and wish to arrange a follow-up meeting at your earliest "
            "convenience to discuss the terms further.\n\n"
            "Please let us know your availability for the week of 24th February.\n\n"
            "Yours sincerely,\nRaj Mehta"
        ),
    },
    {
        "tone": "Formal",
        "text": (
            "Dear Hiring Committee,\n\n"
            "I wish to express my sincere gratitude for the interview opportunity "
            "extended to me on 10th February 2025. It was a privilege to meet the "
            "team and learn more about the organisation's vision.\n\n"
            "I remain enthusiastic about the prospect of contributing to your esteemed "
            "institution and look forward to your decision.\n\n"
            "Respectfully yours,\nAnanya Singh"
        ),
    },
    # ── Friendly ────────────────────────────────────────────────────────────
    {
        "tone": "Friendly",
        "text": (
            "Hey Priya!\n\n"
            "Totally forgot to reply — sorry! Yes, I'm absolutely down for the team "
            "outing on Saturday. Sounds like so much fun! 🎉\n\n"
            "Should I bring anything? Let me know if you need help with planning.\n\n"
            "See you soon,\nRohan"
        ),
    },
    {
        "tone": "Friendly",
        "text": (
            "Hi Kavya,\n\n"
            "Thanks for reaching out! Really great to hear from you. "
            "I'd love to catch up over coffee sometime this week — "
            "let me know what works for you!\n\n"
            "Chat soon,\nDiya"
        ),
    },
    # ── Apologetic ──────────────────────────────────────────────────────────
    {
        "tone": "Apologetic",
        "text": (
            "Dear Mr. Pillai,\n\n"
            "I sincerely apologise for missing the submission deadline. "
            "I take full responsibility for the delay, which was caused by an "
            "unforeseen technical issue on our end.\n\n"
            "I have rectified the problem and the completed report is attached herein. "
            "I assure you this will not recur.\n\n"
            "With deepest apologies,\nSneha Iyer"
        ),
    },
    {
        "tone": "Apologetic",
        "text": (
            "Hi Manish,\n\n"
            "I'm really sorry for the late reply — things have been hectic on my end "
            "and I should have gotten back to you sooner.\n\n"
            "To answer your question: yes, I can attend the meeting on Thursday. "
            "Again, apologies for any inconvenience caused.\n\n"
            "Best,\nPooja"
        ),
    },
    # ── Professional ───────────────────────────────────────────────────────
    {
        "tone": "Professional",
        "text": (
            "Hi Deepthi,\n\n"
            "Thank you for sharing the project update. I have reviewed the milestones "
            "and the team appears to be on track for the Q1 delivery.\n\n"
            "I would recommend scheduling a mid-sprint review by next Friday to "
            "address the open blockers mentioned in Section 3.\n\n"
            "Please confirm once the calendar invite has been sent.\n\n"
            "Best regards,\nArjun Reddy"
        ),
    },
    {
        "tone": "Professional",
        "text": (
            "Dear Ms. Kapoor,\n\n"
            "I am following up on the proposal submitted last week. "
            "Could you please provide an update on the approval status?\n\n"
            "We are keen to proceed as planned and want to ensure the timelines remain intact.\n\n"
            "Looking forward to your response.\n\n"
            "Regards,\nVikram Nair"
        ),
    },
    # ── Appreciative ────────────────────────────────────────────────────────
    {
        "tone": "Appreciative",
        "text": (
            "Dear Team,\n\n"
            "I wanted to take a moment to express my heartfelt appreciation for everyone's "
            "incredible effort during the product launch last week.\n\n"
            "Your dedication, long hours, and collaborative spirit made it a tremendous success. "
            "I am truly proud to work with such a talented group.\n\n"
            "Thank you all so much!\n\nWarm regards,\nSunita Rao"
        ),
    },
    {
        "tone": "Appreciative",
        "text": (
            "Hi Kiran,\n\n"
            "Thank you so much for covering my shifts last week — "
            "I really appreciate your flexibility and team spirit.\n\n"
            "I owe you one! Let me know if there's anything I can help with.\n\n"
            "Cheers,\nAmit"
        ),
    },
    # ── Assertive ───────────────────────────────────────────────────────────
    {
        "tone": "Assertive",
        "text": (
            "Dear Mr. Verma,\n\n"
            "I am writing to bring to your attention that the agreed deliverables for "
            "Phase 2 are now two weeks overdue. This delay is causing cascading impacts "
            "on our downstream teams.\n\n"
            "I require a detailed status update and a revised delivery schedule by "
            "end of business today.\n\n"
            "This matter requires immediate attention.\n\n"
            "Regards,\nNehaa Joshi"
        ),
    },
    # ── Sympathetic ────────────────────────────────────────────────────────
    {
        "tone": "Sympathetic",
        "text": (
            "Dear Rahul,\n\n"
            "I was deeply sorry to hear about your loss. Please know that our thoughts "
            "are with you and your family during this incredibly difficult time.\n\n"
            "Please do not worry about work — take all the time you need. "
            "We are here to support you in any way we can.\n\n"
            "With heartfelt condolences,\nMeera"
        ),
    },
    # ── Informative ────────────────────────────────────────────────────────
    {
        "tone": "Informative",
        "text": (
            "Dear All,\n\n"
            "This is to inform you that the office will remain closed on Monday, "
            "24th February, on account of the public holiday.\n\n"
            "All pending requests should be submitted by Friday, 21st February, "
            "to avoid delays. Normal operations will resume on Tuesday, 25th February.\n\n"
            "For any urgent queries, please contact hr@company.com.\n\n"
            "Regards,\nHR Team"
        ),
    },
    {
        "tone": "Informative",
        "text": (
            "Hi Team,\n\n"
            "Just a quick update: the new onboarding portal is now live at "
            "https://onboard.company.com.\n\n"
            "New joiners should complete their profile, upload documents, and "
            "finish the compliance module within their first three days.\n\n"
            "Let me know if you face any issues.\n\n"
            "Thanks,\nIT Support"
        ),
    },
]


def seed_knowledge_base() -> int:
    """
    Seed the ChromaDB knowledge base with sample emails.
    Already-existing documents are skipped (idempotent).

    Returns the number of newly added documents.
    """
    added = 0
    for item in SEED_EMAILS:
        doc_id = add_email(item["text"], tone=item["tone"], source="seed")
        if doc_id:
            added += 1
    return added


if __name__ == "__main__":
    n = seed_knowledge_base()
    print(f"Seeded {n} email(s) into the knowledge base.")
