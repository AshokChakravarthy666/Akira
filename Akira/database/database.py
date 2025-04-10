from pymongo import MongoClient
from config import Config

class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client[Config.DB_NAME]
        self.users = self.db.users

    async def add_user(self, user_id: int, username: str = None):
        user = {
            "user_id": user_id,
            "username": username
        }
        return self.users.update_one(
            {"user_id": user_id},
            {"$set": user},
            upsert=True
        )

    async def get_user(self, user_id: int):
        return self.users.find_one({"user_id": user_id})

    async def get_all_users(self):
        return self.users.find({})