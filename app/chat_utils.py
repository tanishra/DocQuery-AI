from euriai.langchain import create_chat_model
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.getenv("EURI_API_KEY")

def get_chat_model(api_key: str):
    return create_chat_model(api_key=api_key or API_KEY,
                             model="gpt-4.1-nano",
                             temperature=0.7)
    
    
def ask_chat_model(chat_model, prompt: str):
    response = chat_model.invoke(prompt)
    return response.content