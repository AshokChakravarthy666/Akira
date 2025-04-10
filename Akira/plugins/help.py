from pyrogram import Client, filters

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client, message):
    help_text = """
Available Commands:
/start - Start the bot
/help - Show this help message
    """
    await message.reply_text(help_text)