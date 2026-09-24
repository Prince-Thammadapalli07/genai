import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

URL = os.getenv("LOCAL_HOST_URL")

#In this script I learned about how llms response based on few-shot prompting

#Step-1
#Here I won't add conditions in the script and no telling llm to decide the output based on it.
#Instead we are giving patterns/examples and asking llm to infer the pattern.
#Based on the patterns or examples i gave, it decides the output by analyzing decides the result.
# The Result should be Postive, Negative or Neutral. 
# 1.I ran with harcorded text by changin the prompt every time in the script directly in the text_to_classify.
# 2.Changed it to input() by taking input from the console.
# 3.Tested atlest 3 different scenarios.
# So upto now I have donw LLM -> Text response.

#Step-2
#After the above process i canged the script to get the output in LLM -> structred data -> Python



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

text_to_classify = input("Enter text to classify: ")

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

Return the result as only valid JSON.

The JSON must have exactly this structure.

{{
    "text": "the original text"
    "classification": "Positive, Negative or Neutral"
}}
"""

result = generate_text(prompt)

print(result)