# 🤖 CodeAlpha Basic Chatbot

A rule-based chatbot built in Python that responds to user messages using keyword matching. Built as part of the **CodeAlpha Python Development Internship** (Task 4: Basic Chatbot).

---

## 🚀 Features

- 💬 Keyword-based intent matching
- 🎯 Remembers user's name during the conversation
- ⏰ Tells current time and date
- 😂 Shares programming jokes
- 🧩 Responses stored in external JSON (easy to extend)
- 🛡️ Graceful fallback for unknown inputs
- 🚪 Clean exit with 'bye', 'exit', or 'quit'

---

## 📁 Project Structure

```
CodeAlpha_BasicChatbot/
│
├── src/
│   └── chatbot.py             # Main chatbot logic
├── data/
│   └── responses.json         # Response rules (intents)
├── screenshots/
│   └── demo.png
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🛠️ Requirements

- Python 3.8 or higher
- No external libraries needed

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_BasicChatbot.git
   cd CodeAlpha_BasicChatbot
   ```

2. **Run the chatbot**
   ```bash
   python src/chatbot.py
   ```

3. **Start chatting!**
   ```
   You: hi
   Bot: Hello! How are you doing today?

   You: my name is Ali
   Bot: Nice to meet you, Ali! 😊 How can I help you?

   You: what time is it
   Bot: The current time is 03:45 PM ⏰

   You: bye
   Bot: Goodbye! Have a great day! 👋
   ```

---

## 🧠 How It Works

1. User input is **normalized** (lowercased, punctuation removed).
2. The bot searches for **keywords** defined in `responses.json`.
3. On match → picks a random response from that intent.
4. No match → uses a **fallback** response.
5. Special intents (`time`, `date`) are generated dynamically.

---

## 🧩 Adding New Intents

Just edit `data/responses.json` and add a new block:

```json
"weather": {
  "keywords": ["weather", "temperature"],
  "responses": ["I can't check weather yet, but I'm learning! ☀️"]
}
```

No Python code change needed. 🎉

---

## 📸 Screenshot

![Demo](screenshots/demo.png)

---

## 🔮 Future Improvements

- Add NLP with `nltk` or `spaCy`
- Integrate with a web frontend (Flask/Streamlit)
- Add conversation history / logging
- Multi-language support

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Profile](https://linkedin.com/in/your-profile)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgement

Thanks to **CodeAlpha** for the internship opportunity.