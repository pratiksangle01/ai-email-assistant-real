# AI Email Assistant 🤖📧

> Generate professional, AI-powered email replies in seconds.

---

## ✨ Features

- 🤖 Real AI-powered reply generation via LLM API
- 🔐 Secure API key handling using environment variables
- ⚡ Fast, clean output with minimal setup
- 💼 Built for freelancers, agencies, and support teams

---

## 🧠 How It Works

1. Paste or type a client message
2. The script sends it to the AI API
3. A professional reply is generated instantly
4. Output is printed directly to your terminal

---

## 🛠 Tech Stack

- **Language:** Python 3
- **API:** OpenAI-compatible REST API
- **Library:** `requests`

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pratiksangle01/ai-email-assistant-real.git
cd ai-email-assistant-real
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Set your API key

**macOS / Linux:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
setx OPENAI_API_KEY "your_api_key_here"
```

### 4. Run the script

```bash
python app.py
```

---

## 📌 Example

**Input:**
```
I need help building a website for my business.
```

**Output:**
```
Hi,

Thank you for reaching out! I'd be happy to help you build a website for your business.

Let's connect to discuss your requirements in detail so I can suggest the best solution tailored to your needs.

Looking forward to hearing from you.

Best regards,
[Your Name]
```

---

## 🔐 Security

- API keys are **never** hardcoded in the source
- All credentials are handled via environment variables
- Safe to share or open-source without exposing sensitive data

---

## 🔮 Roadmap

- [ ] Claude API integration
- [ ] Gmail automation (send replies directly)
- [ ] Multi-language support
- [ ] Web UI / browser interface

---

## 💼 Use Cases

- Freelancers responding to client inquiries
- Agencies managing multiple conversations
- Sales outreach and follow-ups
- Customer support automation

---

## 👨‍💻 Author

**Pratik Sangle**  
Feel free to connect or contribute!

---

⭐ If this project helped you, consider giving it a star — it means a lot!
