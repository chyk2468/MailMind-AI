import streamlit as st
import base64
from ai_generator import generate_reply
from rag_engine import add_email, get_kb_count, build_rag_context
from sample_data.sample_emails import seed_knowledge_base

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="MailMind AI ✉️", layout="wide", page_icon="📩")

# ── Seed knowledge base on first run ──────────────────────────────────────────
if "kb_seeded" not in st.session_state:
    seed_knowledge_base()
    st.session_state.kb_seeded = True

# ── Dark Mode Configuration ────────────────────────────────────────────────────
background = "#0d0d0d"
text_color  = "#e8e8e8"
box_bg      = "rgba(20, 20, 30, 0.7)"
accent      = "#4f8ef7"
accent2     = "#7c3aed"
shadow      = "rgba(79,142,247,0.15)"

# ── CSS Styling ────────────────────────────────────────────────────────────────
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        background: {background};
        color: {text_color};
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: rgba(13,13,20,0.95) !important;
        border-right: 1px solid rgba(79,142,247,0.2);
    }}

    .main > div {{
        background: {box_bg};
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2rem 2.5rem;
        box-shadow: 0 8px 40px 0 {shadow};
        margin-top: 10px;
        border: 1px solid rgba(79,142,247,0.12);
    }}

    .title-style {{
        font-size: 42px;
        font-weight: 800;
        display: flex;
        align-items: center;
        gap: 14px;
        background: linear-gradient(135deg, {accent} 0%, {accent2} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: float 3s ease-in-out infinite;
        justify-content: center;
        padding-bottom: 4px;
    }}

    .subtitle-style {{
        font-size: 15px;
        color: rgba(232,232,232,0.55);
        text-align: center;
        margin-bottom: 28px;
        letter-spacing: 0.5px;
    }}

    @keyframes float {{
        0%   {{ transform: translateY(0px);  }}
        50%  {{ transform: translateY(-6px); }}
        100% {{ transform: translateY(0px);  }}
    }}

    textarea {{
        background: #1a1a2e !important;
        color: #e8e8e8 !important;
        border: 1px solid rgba(79,142,247,0.25) !important;
        border-radius: 14px !important;
        padding: 14px !important;
        font-size: 14.5px !important;
        line-height: 1.6 !important;
        font-family: 'Inter', sans-serif !important;
        transition: border 0.3s ease !important;
    }}

    textarea:focus {{
        border: 1px solid {accent} !important;
        box-shadow: 0 0 0 3px rgba(79,142,247,0.15) !important;
    }}

    label {{
        font-size: 14px !important;
        font-weight: 600 !important;
        color: rgba(232,232,232,0.85) !important;
        letter-spacing: 0.3px !important;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, {accent} 0%, {accent2} 100%);
        color: white;
        border: none;
        padding: 0.65rem 1.8rem;
        font-size: 15px;
        font-weight: 600;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(79,142,247,0.35);
        transition: all 0.3s ease;
        width: 100%;
        letter-spacing: 0.4px;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 28px rgba(79,142,247,0.5);
    }}

    .reply-box textarea {{
        animation: slideUp 0.6s ease-out;
        border: 1.5px solid {accent} !important;
    }}

    @keyframes slideUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to   {{ opacity: 1; transform: translateY(0);    }}
    }}

    /* RAG badge */
    .rag-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(79,142,247,0.12);
        border: 1px solid rgba(79,142,247,0.3);
        color: {accent};
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 16px;
    }}

    /* Divider */
    hr {{
        border-color: rgba(79,142,247,0.15) !important;
    }}

    /* Selectbox */
    [data-testid="stSelectbox"] > div > div {{
        background: #1a1a2e !important;
        border: 1px solid rgba(79,142,247,0.25) !important;
        border-radius: 12px !important;
        color: #e8e8e8 !important;
    }}

    @media screen and (max-width: 768px) {{
        .title-style {{ font-size: 28px; }}
        textarea {{ font-size: 13px !important; }}
    }}
    </style>
""", unsafe_allow_html=True)

# ── Sidebar – Knowledge Base Management ───────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div style="padding: 8px 0 16px 0;">
            <div style="font-size:22px; font-weight:700; color:#4f8ef7;">📚 Knowledge Base</div>
            <div style="font-size:12px; color:rgba(232,232,232,0.45); margin-top:4px;">
                RAG-powered email context store
            </div>
        </div>
    """, unsafe_allow_html=True)

    kb_count = get_kb_count()
    st.metric("📄 Stored Emails", kb_count, help="Total emails in your local vector store")

    st.markdown("---")
    st.markdown("**➕ Add Your Own Emails**")
    st.caption("Upload `.txt` files to enrich the knowledge base with your own email style.")

    uploaded_files = st.file_uploader(
        "Upload email(s)",
        type=["txt"],
        accept_multiple_files=True,
        help="Each file should contain one email body.",
    )

    if uploaded_files:
        upload_tone = st.selectbox(
            "Tone label for uploads",
            ["Formal", "Friendly", "Apologetic", "Professional",
             "Appreciative", "Assertive", "Sympathetic", "Informative"],
            key="upload_tone",
        )
        if st.button("📥 Add to Knowledge Base"):
            added = 0
            for f in uploaded_files:
                content = f.read().decode("utf-8", errors="ignore").strip()
                if content:
                    add_email(content, tone=upload_tone, source="upload")
                    added += 1
            st.success(f"✅ Added {added} email(s) to the KB!")
            st.rerun()

    st.markdown("---")
    st.markdown("""
        <div style="font-size:11px; color:rgba(232,232,232,0.35); line-height:1.6;">
            <strong style="color:rgba(232,232,232,0.6);">How RAG works:</strong><br>
            When you generate a reply, MailMind retrieves the most
            semantically similar emails from the KB and injects them
            as context into the Gemini prompt — producing richer,
            more accurate responses.
        </div>
    """, unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
    <div style="text-align:center; padding: 10px 0 4px 0;">
        <div class="title-style">📩 MailMind AI</div>
        <div class="subtitle-style">
            RAG-powered · Gemini 2.0 Flash · 8 Smart Tones
        </div>
        <div style="display:flex; justify-content:center; margin-bottom:8px;">
            <span class="rag-badge">⚡ RAG Enabled</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# ── Columns Layout ─────────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="large")
reply = ""

# ── Left Column ────────────────────────────────────────────────────────────────
with left_col:
    st.markdown("#### 📨 Received Email")
    email_text = st.text_area(
        "Paste the email you received:",
        height=280,
        placeholder=(
            "Subject: Follow-Up on Project Timeline\n\n"
            "Hi [Name],\n\n"
            "Thanks for today's discussion. Could you please send over\n"
            "the revised project timeline by tomorrow?\n\n"
            "Regards,\nSanjay"
        ),
        label_visibility="collapsed",
    )

    tones = {
        "Formal 🏛️":        "Formal",
        "Friendly 😊":       "Friendly",
        "Apologetic 🙏":     "Apologetic",
        "Professional 💼":   "Professional",
        "Appreciative 🙌":   "Appreciative",
        "Assertive 💪":      "Assertive",
        "Sympathetic 💗":    "Sympathetic",
        "Informative 📢":    "Informative",
    }

    st.markdown("#### 🎯 Reply Tone")
    selected = st.selectbox("Choose tone:", list(tones.keys()), label_visibility="collapsed")
    tone = tones[selected]

    st.write("")
    generate = st.button("🚀 Generate Reply")

# ── Right Column ───────────────────────────────────────────────────────────────
with right_col:
    if "generate_clicked" not in st.session_state:
        st.session_state.generate_clicked = False

    if generate:
        if not email_text.strip():
            st.warning("⚠️ Please paste an email to generate a reply.")
        else:
            st.session_state.generate_clicked = True
            with st.spinner("🧠 Retrieving context & generating reply..."):
                # ── RAG: retrieve similar emails ──
                rag_context = build_rag_context(email_text, k=3)
                # ── Generate with enriched prompt ──
                reply = generate_reply(email_text, tone, rag_context=rag_context)
                st.session_state.reply = reply
                st.session_state.rag_used = bool(rag_context)

    if st.session_state.generate_clicked and "reply" in st.session_state:
        st.markdown("#### ✍️ AI-Generated Reply")

        if st.session_state.get("rag_used"):
            st.markdown(
                '<span class="rag-badge">🔍 Context retrieved from KB</span>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="reply-box">', unsafe_allow_html=True)
        st.text_area(
            "Your reply:",
            value=st.session_state.reply,
            height=280,
            label_visibility="collapsed",
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Copy to Clipboard ──────────────────────────────────────────────
        st.markdown("""
            <div style="display:flex; gap:12px; margin-top:14px; align-items:center;">
                <button onclick="copyReply()" style="
                    background: linear-gradient(135deg,#22c55e,#16a34a);
                    color:white; border:none; padding:9px 20px;
                    border-radius:10px; cursor:pointer; font-size:14px;
                    font-weight:600; letter-spacing:0.3px;
                    box-shadow:0 4px 14px rgba(34,197,94,0.3);">
                    📋 Copy to Clipboard
                </button>
                <span id="copy-msg" style="font-size:13px; color:#22c55e;
                    opacity:0; transition:all 0.3s ease; transform:translateY(-8px);">
                    ✅ Copied!
                </span>
            </div>

            <script>
            function copyReply() {
                const textareas = window.parent.document.querySelectorAll('textarea');
                const replyBox  = textareas[textareas.length - 1];
                if (replyBox) {
                    navigator.clipboard.writeText(replyBox.value).then(function() {
                        const msg = document.getElementById("copy-msg");
                        msg.style.opacity  = 1;
                        msg.style.transform = "translateY(0)";
                        setTimeout(() => {
                            msg.style.opacity  = 0;
                            msg.style.transform = "translateY(-8px)";
                        }, 1800);
                    });
                }
            }
            </script>
        """, unsafe_allow_html=True)

        # ── Download as .txt ───────────────────────────────────────────────
        b64  = base64.b64encode(st.session_state.reply.encode()).decode()
        href = f"""
            <div style="margin-top:12px;">
                <a href="data:file/txt;base64,{b64}" download="mailmind_reply.txt"
                style="color:{accent}; font-weight:600; font-size:14px;
                       text-decoration:none; border:1.5px solid {accent};
                       padding:8px 18px; border-radius:10px; display:inline-block;
                       transition:all 0.3s ease;">
                    📥 Download as .txt
                </a>
            </div>
            <style>
            a[download]:hover {{
                background:{accent};
                color:#0d0d0d !important;
            }}
            </style>
        """
        st.markdown(href, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div style='text-align:center; padding:8px 0; font-size:13px; color:rgba(232,232,232,0.4);'>"
    "Made with ❤️ by <strong style='color:rgba(232,232,232,0.7);'>Ch. Yashwant Kumar</strong>"
    " &nbsp;·&nbsp; Powered by Gemini 2.0 Flash &amp; ChromaDB RAG"
    "</div>",
    unsafe_allow_html=True,
)
