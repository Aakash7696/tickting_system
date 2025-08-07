# app/db.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Live Mongo Database URL from .env file
MONGO_DATABASE_URL = os.getenv("MONGO_DATABASE_URL")

# Create an instance of the MongoClient

# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient(MONGO_DATABASE_URL)

# Access the database
db = client["ticket_system"]

# Collection names (equivalent to tables in relational databases)
tickets_collection = db["tickets"]
