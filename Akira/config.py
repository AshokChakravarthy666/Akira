import os
from dotenv import load_dotenv

load_dotenv()  

API_ID = int(os.getenv("API_ID", "your_api_id"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token") 
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://<username>:<password>@cluster0.mongodb.net/akira_bot_db?retryWrites=true&w=majority")
ADMINS = os.getenv("ADMINS", "123456789,987654321")

