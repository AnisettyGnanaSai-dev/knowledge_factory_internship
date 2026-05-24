from pymongo import MongoClient

from config.settings import (
    MONGO_URL,
    DATABASE_NAME,
    COLLECTION_NAME
)

client = MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=3000
)

db = client[DATABASE_NAME]

request_collection = db[COLLECTION_NAME]