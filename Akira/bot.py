import logging
import os
import importlib
from pyrogram import Client
from Akira.config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Client("AkiraBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Automatically import all files from the Akira folder (assuming command files are directly in the Akira folder)
commands_directory = os.path.dirname(__file__)  # The Akira folder itself

# Loop through the Akira folder and import each Python file (command)
for filename in os.listdir(commands_directory):
    if filename.endswith(".py") and filename != "__init__.py" and filename != "bot.py" and filename != "config.py" and filename != "__main__.py":
        module_name = f"Akira.{filename[:-3]}"  # Remove the .py extension
        importlib.import_module(module_name)  # Import the command dynamically
        logging.info(f"Loaded command handler: {module_name}")


def main():
    logger.info("Bot is starting...")
    app.run()
