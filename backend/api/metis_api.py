import logging

import requests
from colorama import Fore, Style

from config import METIS_API_KEY, METIS_PROVIDER_URL


def send_request(messages: list):
    """
    Send the request to Metis API and return the response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": METIS_API_KEY,
    }

    payload = {
        "model": "gpt-3.5-turbo-0125",
        "messages": messages,
        "max_tokens": 100,
    }

    try:
        response = requests.post(METIS_PROVIDER_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API request: {e}")
        return None
