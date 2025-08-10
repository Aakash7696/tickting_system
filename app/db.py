from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DATABASE_URL = os.getenv("MONGO_DATABASE_URL")
print(f"Connecting to MongoDB at {MONGO_DATABASE_URL}")

client = MongoClient(MONGO_DATABASE_URL)
print("MongoDB client created:- ", client)

try:
    client.admin.command('ping')
    print("✅ MongoDB connection successful.")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

db = client["ticket_system"]
tickets_collection = db["tickets"]

# ----------------------------
# If you want to use Local Mongo instead, uncomment this:
# client = MongoClient("mongodb://localhost:27017/")
# db = client["ticket_system"]
# tickets_collection = db["tickets"]
# ----------------------------
