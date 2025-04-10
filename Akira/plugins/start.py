from pyrogram import Client, filters
from Akira.database.database import Database

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        f"Hello {message.from_user.mention}! 👋\n"
        "Welcome to my bot."
    )