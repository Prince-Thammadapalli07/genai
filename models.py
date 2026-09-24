import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")  # replace with your key

def list_gemini_models():
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        print("Available models:\n")
        for model in data.get("models", []):
            print(f"- {model['name']}")
            print(f"  Supported methods: {model.get('supportedGenerationMethods', [])}")
            print()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    list_gemini_models()
