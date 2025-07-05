import streamlit as st
import base64
from ai_generator import generate_reply
st.set_page_config(page_title="MailMind AI ✉️", layout="centered")
# ---------- Dark Mode Configuration ----------
background = "#121212"
text_color = "#ffffff"
box_bg = "rgba(30, 30, 30, 0.4)"
shadow = "rgba(255,255,255,0.1)"
emoji_bg = "#ffffff"
emoji_color = "#000000"

# ---------- CSS Styling ----------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
        background: {background};
        color: {text_color};
    }}

    .main > div {{
        background: {box_bg};
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 {shadow};
        margin-top: 20px;
    }}

    .title-style {{
        font-size: 36px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 12px;
        animation: float 3s ease-in-out infinite;
        padding-bottom: 10px;
        justify-content: center;
    }}

    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-8px); }}
        100% {{ transform: translateY(0px); }}
    }}

    .emoji-badge {{
        background-color: {emoji_bg};
        color: {emoji_color};
        padding: 8px 10px;
        border-radius: 50%;
        font-size: 22px;
        display: inline-block;
    }}

    .subtitle-style {{
        font-size: 18px;
        color: {text_color};
        padding-bottom: 20px;
        text-align: center;
    }}

    textarea {{
        background: #2e2e2e !important;
        color: #ffffff !important;
        box-shadow: 4px 4px 12px #1a1a1a, -4px -4px 12px #3a3a3a !important;
        border-radius: 15px !important;
        padding: 12px !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
    }}

    label {{
        font-size: 22px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }}

    .stButton>button {{
        background-color: #2c83f2;
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        font-size: 16px;
        border-radius: 12px;
        box-shadow: 0 4px 14px rgba(44, 131, 242, 0.4);
        transition: all 0.3s ease;
    }}

    .stButton>button:hover {{
        background-color: #3b90ff;
        transform: translateY(-3px);
    }}

    .reply-box textarea {{
        animation: slideUp 0.8s ease-out;
        border: 2px solid #2c83f2;
    }}

    @keyframes slideUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @media screen and (max-width: 768px) {{
        .title-style {{ font-size: 28px; flex-direction: column; align-items: flex-start; }}
        textarea {{ font-size: 14px !important; }}
    }}

    .copy-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        margin-top: 20px;
        flex-direction: column;
    }}

    .copy-btn {{
        background-color: #28a745;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 15px;
    }}

    .copy-msg {{
        font-size: 14px;
        color: #00ff8c;
        opacity: 0;
        transition: all 0.3s ease-in-out;
        transform: translateY(-10px);
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown(f"""
    <div style="text-align: center; padding-top: 10px;">
        <div class="title-style">
            <span class="emoji-badge">📩</span>
            MailMind AI
        </div>
    </div>
""", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
# ---------- Columns Layout ----------
left_col, right_col = st.columns(2)
reply = ""

# ---------- Left Column ----------
with left_col:
    email_text = st.text_area(
        "📨 Paste the received email below:",
        height=260,
        placeholder="e.g., Subject: Follow-Up...\n\nBody:\nHi Priya,\nThanks for today’s discussion..."
    )

    tones = {
        "Formal 🏛️": "Formal",
        "Friendly 😊": "Friendly",
        "Apologetic 🙏": "Apologetic",
        "Professional 💼": "Professional",
        "Appreciative 🙌": "Appreciative",
        "Assertive 💪": "Assertive",
        "Sympathetic 💗": "Sympathetic",
        "Informative 📢": "Informative"
    }
    selected = st.selectbox("🎯 Choose a reply tone:", list(tones.keys()))
    tone = tones[selected]

    generate = st.button("🚀 Generate Reply")

# ---------- Right Column ----------
with right_col:
    if 'generate_clicked' not in st.session_state:
        st.session_state.generate_clicked = False

    if generate:
        if not email_text.strip():
            st.warning("⚠️ Please paste an email to generate a reply.")
        else:
            st.session_state.generate_clicked = True
            with st.spinner("🧠 Thinking..."):
                reply = generate_reply(email_text, tone)
                st.session_state.reply = reply

    if st.session_state.generate_clicked and 'reply' in st.session_state:
        st.markdown('<div class="reply-box">', unsafe_allow_html=True)
        st.text_area("✍️ Your AI-generated reply:", value=st.session_state.reply, height=260)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- Copy to Clipboard Button with JS Popup ----------
        st.markdown("""
            <div class="copy-container">
                <button onclick="copyReply()" class="copy-btn">📋 Copy to Clipboard</button>
                <span id="copy-msg" class="copy-msg">✅ Copied!</span>
            </div>

            <script>
            function copyReply() {
                const replyBox = document.querySelectorAll('textarea')[1];
                if (replyBox) {
                    navigator.clipboard.writeText(replyBox.value).then(function() {
                        const msg = document.getElementById("copy-msg");
                        msg.style.opacity = 1;
                        msg.style.transform = "translateY(0)";
                        setTimeout(() => {
                            msg.style.opacity = 0;
                            msg.style.transform = "translateY(-10px)";
                        }, 1500);
                    });
                }
            }
            </script>
        """, unsafe_allow_html=True)

        # ---------- Download as .txt ----------
        b64 = base64.b64encode(st.session_state.reply.encode()).decode()
        href = f"""
            <div style='display: flex; justify-content: center; align-items: center; margin-top: 15px;'>
                <a href="data:file/txt;base64,{b64}" download="reply.txt"
                style="color: #2c83f2; font-weight: 600; font-size: 15px; text-decoration: none;
                       border: 2px solid #2c83f2; padding: 8px 16px; border-radius: 8px;
                       transition: all 0.3s ease; display: inline-block;">
                    📥 Download reply as .txt
                </a>
            </div>
            <style>
            a:hover {{
                background-color: #2c83f2;
                color: white !important;
            }}
            </style>
        """
        st.markdown(href, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; padding-top: 10px;'>"
    "Made with ❤️ by <strong>Ch. Yashwant Kumar</strong>"
    "</div>",
    unsafe_allow_html=True
)
