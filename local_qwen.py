import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

URL = os.getenv("LOCAL_HOST_URL")

def generate_text(prompt):

    url = URL

    payload = {
        "model": "qwen3:8b",
        "prompt": prompt,
        "stream": False
    }   

    response = requests.post(url, json=payload)

    if response.status_code == 200:
       data = response.json()
       return response.json()["response"]
    else:
       raise Exception(f"Error {response.status_code}: {response.text}")

text_to_classify = "The performance of this laptop is disappointing."

prompt = f"""
You are a sentiment classification assistant.

Classify the sentiment as Positive, Negative, or Neutral.

Examples:

Text: "The laptop is excellent."
Sentiment: Positive

Text: "The laptop is terrible."
Sentiment: Negative

Text: "The laptop is okay."
Sentiment: Neutral

Now classify this text:

"{text_to_classify}"

Return only the sentiment.
"""

result = generate_text(prompt)

print(result)