Welcome To Telly Bot

# Telly Bot 🤖
Your friendly Telegram AI Assistant — Ask anything, get instant answers, and even generate images!  
Powered by Python, Flask, and the OpenAI API (with API key support from BoltIOT).

---

## 🚀 About
Telly Bot is a Telegram bot that can:
- ✅ Answer any kind of question instantly.
- 🎨 Generate AI-powered images from text prompts.
- 💬 Respond to commands like `/start` and `/help`.
- 🌐 Available 24/7, deployed on Render.

This bot is built using:
- **Python**
- **Flask**
- **BotFather** (for Telegram bot setup)
- **OpenAI API**
- **Render** (for deployment)
- **BoltIOT** (for API key support)

---

## 📌 Try It Now
Click here to chat with Telly Bot: [Telly Bot on Telegram](https://t.me/Pllaayy_bot)

---

## 🛠 Features
| Feature              | Description |
|----------------------|-------------|
| Ask Anything         | Type any question, get quick and accurate answers. |
| AI Image Generation  | Send a text description and get an AI-generated image. |
| Command Support      | `/start` and `/help` to guide new users. |
| Always Online        | Hosted on Render for 24/7 availability. |

---

## ⚙️ How It Works
1. User sends a message or command to the bot on Telegram.
2. Flask server receives and processes the request.
3. OpenAI API generates the answer or image.
4. Bot sends the response back to the user instantly.

---

## 💻 Local Setup (Optional for Developers)
If you want to run Telly Bot locally:
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/telly-bot.git
cd telly-bot

# Install dependencies
pip install -r requirements.txt

# Create .env file and add:
# BOT_TOKEN=your_telegram_bot_token
# OPENAI_API_KEY=your_openai_api_key

# Run the bot
python main.py
