import requests

url = "https://jsonplaceholder.typicode.com/users"

data = {
    "name": "Gnani",
    "username": "gnani123",
    "email": "gnani123@example.com"
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Check for HTTP errors
    if response.status_code == 201:
        created_user = response.json()
        print(f"User created successfully: {created_user}")
    else:
        print(f"Failed to create user. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")