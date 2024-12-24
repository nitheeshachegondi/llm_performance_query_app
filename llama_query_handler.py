import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Groq API endpoint and credentials
LLM_API_URL = os.getenv("LLM_API_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

def handle_query(user_query):
    data = {
        "query": user_query
    }

    # API call to Groq LLM
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(LLM_API_URL, json=data, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error with LLM API: {response.text}")

    # Extract relevant details from LLM response
    response_data = response.json()
    entities = response_data.get("entities", [])
    parameters = response_data.get("parameters", [])
    
    return entities, parameters
