import os

from dotenv import load_dotenv

load_dotenv()

METIS_API_KEY = os.getenv("METIS_API_KEY")
METIS_PROVIDER_URL = os.getenv("METIS_PROVIDER_URL")
