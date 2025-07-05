import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAbZMi0GpUmeqW5_L7rm3lGps4su1nTdnE"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_reply(email_text, tone):
    prompt = (
        f"You are an AI assistant that helps write professional email replies.\n"
        f"Received Email:\n\"{email_text}\"\n\n"
        f"Write a {tone.lower()} reply to this email. "
        f"The tone must be clearly reflected. Keep it concise, polite, and relevant."
    )
    response = model.generate_content(prompt)
    return response.text.strip()
