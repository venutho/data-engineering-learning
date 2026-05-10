import requests
import psycopg2

API_URL = "https://jsonplaceholder.typicode.com/users"

connection = psycopg2.connect(
    host="localhost",
    database="de_learning",
    user="postgres",
    password="postgres"
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