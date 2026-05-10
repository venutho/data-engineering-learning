import requests
import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://jsonplaceholder.typicode.com/users"

connection = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432"),
    database=os.getenv("DB_NAME", "de_learning"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD", "postgres")
)

cursor = connection.cursor()

response = requests.get(API_URL, timeout=10)
response.raise_for_status()

users = response.json()

for user in users:
    cursor.execute(
        """
        INSERT INTO users (id, name, email, city, company)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """,
        (
            user["id"],
            user["name"],
            user["email"],
            user["address"]["city"],
            user["company"]["name"]
        )
    )

connection.commit()

cursor.close()
connection.close()

print("Users loaded successfully!")