import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")  # <-- replace with your API key
MODEL = "models/gemini-3.6-flash"    # <-- pick one from your list (e.g., gemini-2.5-flash or gemini-2.5-pro)

def generate_text(prompt: str) -> str:
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": 
                [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            # "responseSchema": {
            #     "type": "OBJECT",
            #     "properties": {
            #         "definition": {
            #             "type": "STRING"
            #         },
            #         "analogy": {
            #             "type": "STRING"
            #         },
            #         "technical_example": {
            #             "type": "STRING"
            #         },
            #         "java_example": {
            #             "type": "STRING"
            #         }
            #     },
            #     "required": [
            #         "definition",
            #         "analogy",
            #         "technical_example",
            #         "java_example"
            #     ]
            # }
        }
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return json.loads(data["candidates"][0]["content"]["parts"][0]["text"])
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":

    text_to_classify = "The product arrived yesterday."

    result = generate_text(
        f"""
        You are a sentiment classification assistant.

        Classify the sentiment as Positive, Negative or Neutral.

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
    )
    print(result)