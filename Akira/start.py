from pyrogram import filters
from Akira.bot import app
from Akira.db.mongo import users

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    user = await users.find_one({"chat_id": user_id})
    if not user:
        await users.insert_one({"chat_id": user_id, "first_name": first_name})

    welcome_text = f"""
👋 Hello {first_name}!

Welcome to the Akira Bot. Use /help to see available commands.
"""
    await message.reply(welcome_text)
