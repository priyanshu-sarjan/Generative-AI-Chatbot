import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB connection string from environment variables
MONGO_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB
# Make sure your MONGODB_URI is set correctly in your .env file!
try:
    client = MongoClient(MONGO_URI)
    # Create or connect to a database named "study_bot_db"
    db = client["study_bot_db"]  
    # Create or connect to a collection called "chat_history"
    chat_collection = db["chat_history"] 
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

def save_chat_message(user_id: str, role: str, content: str):
    """
    Stores a single message in MongoDB.
    'role' should be either 'user' or 'bot'.
    """
    message_data = {
        "user_id": user_id,
        "role": role,        
        "content": content
    }
    chat_collection.insert_one(message_data)

def get_chat_history(user_id: str, limit: int = 10):
    """
    Retrieves previous messages for a specific user to provide context.
    We limit it to the last 10 messages so we don't overwhelm the LLM's context window.
    """
    # Find messages for the user, sort by insertion order (oldest to newest)
    # _id in MongoDB contains a timestamp naturally, so sorting by _id works perfectly.
    cursor = chat_collection.find({"user_id": user_id}).sort("_id", 1).limit(limit)
    
    history = []
    for doc in cursor:
        history.append({
            "role": doc["role"],
            "content": doc["content"]
        })
    
    return history
