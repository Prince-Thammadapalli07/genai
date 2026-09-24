from google.oauth2 import service_account
import google.auth.transport.requests
import requests

def call_gemini_flash(prompt: str) -> str:
    # Load service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        "D:/genai/venv/genaiproject-508016-d26fa5d445ac.json",  # <-- replace with the path to your JSON file
        scopes=["https://www.googleapis.com/auth/generative-language"]
    )

    # Refresh to get an access token    
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    access_token = credentials.token

    # Gemini Flash endpoint
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


# Example usage
if __name__ == "__main__":
    print(call_gemini_flash("Write a short poem about the stars."))
