from pyrogram import filters
from Akira.bot import app

@app.on_message(filters.command("ping"))
async def ping_handler(client, message):
    await message.reply("🏓 Pong!")
