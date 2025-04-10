from pyrogram import Client
from config import Config

app = Client(
    "TelegramBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Akira/plugins")
)

if __name__ == "__main__":
    app.run()