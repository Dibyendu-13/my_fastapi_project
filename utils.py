import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LLM_API_URL = os.getenv("LLM_API_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

def get_technology_company_label(description: str) -> str:
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"inputs": description}
    response = requests.post(LLM_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        # Assuming the model returns predictions in a list format
        labels = [item['label'] for item in result]
        return "Yes" if "technology" in labels else "No"
    else:
        return "No"
