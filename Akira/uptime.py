import time
from pyrogram import filters
from Akira.bot import app  # This ensures the bot's app instance is accessible

# Store the bot's start time
bot_start_time = time.time()

@app.on_message(filters.command("uptime"))
async def uptime_handler(client, message):
    """Respond with the bot's uptime."""
    uptime_seconds = time.time() - bot_start_time
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    uptime_seconds = int(uptime_seconds % 60)

    uptime_message = f"Bot has been running for {uptime_hours} hours, {uptime_minutes} minutes, and {uptime_seconds} seconds."
    
    await message.reply(uptime_message)
