from pyrogram import filters
from Akira.bot import app

@app.on_message(filters.command("userinfo"))
async def userinfo_handler(client, message):
    user = message.from_user

    info_text = f"""
👤 **User Info**
🆔 ID: `{user.id}`
📛 Name: {user.first_name}
🔗 Username: @{user.username if user.username else "N/A"}
🌐 Language: {user.language_code if user.language_code else "Unknown"}
"""

    await message.reply(info_text)
