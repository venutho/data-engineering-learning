import requests
import os
from dotenv import load_dotenv
from python_refresh.config.logger_config import logger

load_dotenv()

API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com")
USERS_ENDPOINT = API_URL + "/users"

def fetch_users():
    logger.info("Fetching users from API")
    response = requests.get(USERS_ENDPOINT, timeout=10)
    response.raise_for_status()

    logger.info("Successfully fetched users")

    return response.json()