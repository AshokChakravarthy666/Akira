import motor.motor_asyncio
from Akira.config import MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

db_name = "Akira" 
db = client[db_name] 

users = db.users 