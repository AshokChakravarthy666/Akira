from pyrogram import filters
from Akira.bot import app

@app.on_message(filters.command("help"))
async def help_handler(client, message):
    help_text = """
👋 **Available Commands**:
/start - Start the bot and register yourself.
/help - Show this help message.
/broadcast [message] - (Admins only) Send a broadcast to all users.

📌 More features coming soon...
"""
    await message.reply(help_text)
