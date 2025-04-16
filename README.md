# Akira Telegram Bot

A **modular and scalable** Telegram bot built using **Pyrogram** and **MongoDB**. The bot is designed to be easily extended, with a clean architecture that supports adding new features via separate Python modules.

---

## Deploy to Heroku

Click the button below to deploy **Akira Telegram Bot** to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yourusername/akira-bot)

---

## Features

- Scalable and modular architecture.
- Supports media broadcasting (text, photos, videos, documents).
- Broadcast to thousands of users with throttling to avoid rate limits.
- Admin-only commands (e.g., broadcast, user info).
- MongoDB backend for persistent storage of user data.
- Easy to extend by adding new features in separate files.

---

## Requirements

Before deploying, you need to have:

- **Telegram Bot Token** from [BotFather](https://core.telegram.org/bots#botfather).
- **Telegram API ID and API Hash** from [my.telegram.org](https://my.telegram.org/auth).
- **MongoDB URI** for connecting to a MongoDB database.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/akira-bot.git
   cd akira-bot
   ```
