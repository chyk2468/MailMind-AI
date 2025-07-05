# ✉️ MailMind AI — Smart Email Reply Generator using Gemini 2.0 Flash

MailMind AI is an advanced email reply generator that uses **Google Gemini 2.0 Flash API** to generate high-quality, tone-specific responses to received emails. It features a beautiful, animated dark-mode UI built with **Streamlit**, and empowers users to communicate efficiently with the right tone for any context — be it professional, friendly, or assertive.

---

## 🌟 Key Features

- 🎯 **Smart Tone Selection**  
  Choose from 8 emotionally aware tones — Formal, Friendly, Apologetic, Professional, Appreciative, Assertive, Sympathetic, and Informative.

- 💡 **Generative AI Power**  
  Powered by **Gemini 2.0 Flash**, a fast and smart language model by Google, to create accurate, clear, and concise replies.

- 🖌️ **Modern UI/UX Design**  
  Built with custom CSS for a dark-glass effect, animated text fields, and responsive layout — delivering an elegant user experience.

- 📋 **Copy to Clipboard**  
  Instantly copy your AI-generated email with one click and a stylish visual confirmation.

- 📥 **Download as .txt File**  
  Save your generated replies to a `.txt` file with a centered, themed download button.

- 🖥️ **Responsive Design**  
  Fully responsive layout for both desktop and mobile screens.

---

## 🛠️ Technologies Used

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python + [Google Generative AI API](https://ai.google.dev/)
- **AI Model**: `gemini-2.0-flash`
- **Styling**: Custom CSS with animations, Google Fonts (Poppins)

---

## 📁 Project Structure

```

MailMind-AI/
│
├── app.py               # Streamlit frontend and app logic
├── ai_generator.py      # Reply generation using Gemini 2.0 Flash
├── README.md            # Project documentation (this file)
├── requirements.txt     # Required Python packages
└── .streamlit/
└── config.toml      # Optional Streamlit theme config

```

---

## 🧠 How It Works

1. The user pastes an email received from someone else.
2. Selects a tone of reply (e.g., Formal, Friendly, Apologetic).
3. Clicks the "Generate Reply" button.
4. The app sends the prompt to Gemini 2.0 Flash via Google Generative AI API.
5. A smart, tone-specific reply is generated and displayed with UI effects.
6. The user can then copy it or download it as a `.txt` file.

---

## 📸 Sample Screenshot
Step-1:- inter face
![Step-1 Screenshot](https://github.com/user-attachments/assets/4cec8aca-c203-4c68-9940-7a0fd513b19a)

Step-2:- past the mail and click Generate Reply button
![Step-2 Screenshot](https://github.com/user-attachments/assets/75f45176-3624-4c07-b0be-6a4cd35eb1cb)

Step-3:- Reply Mail is Generated
![Step-3 Screenshot](https://github.com/user-attachments/assets/2fb3fccf-83d1-44af-ae7d-a584b6e35594)



---

## 🧪 Example Use Case

### ✉️ Input Email:
```

Hi Priya,

Thanks for today’s discussion. Can you send over the revised project timeline by tomorrow?

Regards,
Sanjay

```

### 🎯 Tone: Appreciative

### 🤖 AI-Generated Reply:
```

Hi Sanjay,

Thank you for the engaging discussion today. I appreciate your clarity and insights.
I’ll make sure to share the updated project timeline with you by tomorrow.

Best regards,
Priya

````

---

## ⚙️ How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/mailmind-ai.git
cd mailmind-ai
````

2. **Install Required Packages**

```bash
pip install -r requirements.txt
```

3. **Set Your Google API Key**

Modify `ai_generator.py` to load the key from environment:

```python
import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```

Set it in terminal:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

4. **Run the Streamlit App**

```bash
streamlit run app.py
```

---

## 🔐 Security Note

Never expose your API keys publicly. Use environment variables or `.env` files, and ensure `.env` is included in `.gitignore`.

---

## 📦 Requirements

```
streamlit
google-generativeai
```

---

## 👨‍💻 Author

Made with ❤️ by **Ch. Yashwant Kumar**

---

Enjoy the ✨ power of AI-assisted communication with **MailMind AI**!
