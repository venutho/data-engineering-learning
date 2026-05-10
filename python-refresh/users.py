import requests

URL = 'https://jsonplaceholder.typicode.com/users'

try:
    response = requests.get(URL, timeout=10)  
    response.raise_for_status()  
    users = response.json()
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")
except requests.RequestException as e:
    print(f"Error fetching users: {e}")