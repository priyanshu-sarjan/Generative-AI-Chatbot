from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Import the logic from the other files in your repository
# Make sure database.py and bot_logic.py are in the same folder!
from database import save_chat_message, get_chat_history
from bot_logic import get_study_bot_response

# Initialize the FastAPI app
app = FastAPI(
    title="Study Bot API", 
    description="An AI-powered chatbot that helps users ask questions related to study topics."
)

# Define the structure for incoming user requests
class ChatRequest(BaseModel):
    user_id: str   # A unique ID to track the user's specific conversation memory
    message: str   # The user's study question

# A simple root endpoint to verify the API is running
@app.get("/")
def read_root():
    return {"status": "Study Bot API is running!"}

# The main chat endpoint
@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    try:
        # 1. Retrieve previous messages from MongoDB to provide context-aware responses
        chat_history = get_chat_history(request.user_id)
        
        # 2. Pass the new message and history to the LLM to get an answer
        bot_response = get_study_bot_response(request.message, chat_history)
        
        # 3. Store both the user's message and the bot's response in MongoDB
        save_chat_message(request.user_id, "user", request.message)
        save_chat_message(request.user_id, "bot", bot_response)
        
        # 4. Return the final response to the user
        return {"response": bot_response}
        
    except Exception as e:
        # If anything fails (like the MongoDB connection or Groq API), return an error
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Use Uvicorn to run the server if the script is executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
