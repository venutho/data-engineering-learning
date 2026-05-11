import requests
import os
from dotenv import load_dotenv
from python_refresh.config.logger_config import logger

load_dotenv()

API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com")
COMMENTS_ENDPOINT = API_URL + "/comments"



def fetch_comments():
    logger.info("Fetching comments from API")
    response = requests.get(COMMENTS_ENDPOINT, timeout=10)
    response.raise_for_status()

    logger.info("Successfully fetched comments")

    return response.json()