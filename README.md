# Generative-AI-Chatbot
# Study Bot - AI Study Assistant

## Project Overview
Study Bot is an AI-powered chatbot designed to help users ask questions related to academic and study topics[cite: 178, 196]. [cite_start]Built using a FastAPI backend, this project leverages LangChain and the Groq LLM API to provide intelligent, context-aware responses[cite: 181, 185]. [cite_start]The bot is designed to act strictly as a study assistant, utilizing a custom system prompt to guide its behavior and gently redirect off-topic questions[cite: 195].

## Hosted API Link
[cite_start]**Live API URL:** `[Paste your Render .onrender.com link here]` [cite: 203]
**API Documentation (Swagger UI):** `[Paste your Render link here]/docs`

## Memory Implementation
[cite_start]To ensure the chatbot remembers previous conversations, this project integrates MongoDB for persistent data storage[cite: 178, 180]. 
* [cite_start]**Storage:** Every interaction is saved to a `chat_history` collection in MongoDB, storing the `user_id`, `role` (user or bot), and the `content` of the message[cite: 192].
* [cite_start]**Context Retrieval:** When a user sends a new message, the backend retrieves the last 10 messages for that specific `user_id` from the database[cite: 193]. 
* [cite_start]**Integration:** This history is formatted into LangChain message objects and passed alongside the new prompt to the LLM, allowing the AI to maintain context and provide conversational, memory-aware answers[cite: 182].

## Tech Stack
* [cite_start]**Framework:** FastAPI & Uvicorn [cite: 185]
* [cite_start]**AI/LLM:** LangChain & ChatGroq (Llama 3) [cite: 185, 188]
* [cite_start]**Database:** MongoDB (using PyMongo) [cite: 190, 191]
* [cite_start]**Deployment:** Render [cite: 198]

## Local Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/study-bot.git](https://github.com/yourusername/study-bot.git)
   cd study-bot

pip install -r requirements.txt



GROQ_API_KEY=your_api_key
MONGODB_URI=your_mongodb_connection_string



python main.py







   pip install -r requirements.txt
