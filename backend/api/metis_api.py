import requests
from config import METIS_API_KEY, METIS_PROVIDER_URL

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": METIS_API_KEY,
}


def send_request(messages, max_tokens=100):
    """Send a chat request to Metis AI and return the assistant's response."""
    payload = {
        "model": "gpt-3.5-turbo-0125",
        "messages": messages,
        "max_tokens": max_tokens,
    }

    response = requests.post(METIS_PROVIDER_URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        bot_response = response.json()
        return bot_response["choices"][0]["message"]["content"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
