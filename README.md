# 🚀 Telegram Group Moderator Bot  

<p align="center">
  <img src="https://i.ibb.co/zVVZ845q/welcome-image.jpg" alt="Bot Banner" width="500"/>
</p>

<p align="center">
  <b>A powerful Telegram group moderation bot built with <a href="https://docs.aiogram.dev/">Aiogram</a></b>  
</p>

---

## ✨ Features

- 🎉 **Welcome System** – New members get a custom welcome message with:
  - Username, User ID, Full Name
  - Join Date & Time  
  - Group Name  
  - Welcome Image + Notes Hub Button  

- 🔒 **Admin Commands**  
  - `/ban` – Ban a user (use by replying to their message)  
  - `/unban <user_id>` – Unban a user with ID  
  - `/mute` – Mute a user for 1 hour  
  - `/unmute` – Remove mute from a user  
  - `/kick` – Kick a user (removes and unbans instantly)  

- 🛡️ **Admin Check** – Only admins can use moderation commands.  

---

## 🖼️ Demo (Welcome Message)
<p align="center">
  <img src="https://i.ibb.co/zVVZ845q/welcome-image.jpg" alt="Welcome Demo" width="400"/>
</p>

---

## ⚡ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Cypher-Squad/telegram-moderator-bot.git
   cd telegram-moderator-bot
   ```

2. Install dependencies:
   ```bash
   pip install aiogram
   ```

3. Create a bot with [@BotFather](https://t.me/BotFather) and get your API Token.  

4. Replace this line in `bot.py` with your token:
   ```python
   API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

---

## 📜 Example Usage

- Add the bot to your group.  
- Promote it as **Admin** with rights to ban/mute users.  
- Try commands:  
  ```
  /ban (reply to user message)
  /unban 12345678
  /mute (reply to user message)
  /unmute (reply to user message)
  /kick (reply to user message)
  ```

---

## 👨‍💻 Author
- **Cypher Squad**  
- Telegram: [@Cypher_Squad](https://t.me/GODXGENSHIN)  
- GitHub: [Cypher-Squad](https://github.com/Cypher-Squad)  

---
