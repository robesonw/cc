from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongo_url)

def get_database():
    return client[settings.mongo_db]

def get_collection(db, name: str):
    return db[name]
