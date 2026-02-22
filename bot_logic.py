import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables (API keys)
load_dotenv()

# 1. Initialize the Groq LLM
# You can change the model_name to "llama3-8b-8192" or another supported Groq model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile", 
    temperature=0.5
)

# 2. Define the System Prompt
system_prompt = """
You are Study Bot, an AI-powered academic assistant. 
Your goal is to help students answer questions related to their study topics.
Explain complex concepts clearly and step-by-step.
If a user asks about non-academic topics, gently remind them that you are a study assistant.
"""

# 3. Create the prompt template with a placeholder for the chat memory
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

# 4. Create the Langchain pipeline
study_chain = prompt_template | llm

def get_study_bot_response(user_message: str, history_list: list):
    """
    Takes the new user message and the database history to generate a context-aware answer.
    """
    # Convert the raw dictionary history from MongoDB into LangChain message objects
    formatted_history = []
    for msg in history_list:
        if msg["role"] == "user":
            formatted_history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "bot":
            formatted_history.append(AIMessage(content=msg["content"]))
            
    # Invoke the LLM with the formatted history and the new question
    response = study_chain.invoke({
        "chat_history": formatted_history,
        "user_input": user_message
    })
    
    return response.content
