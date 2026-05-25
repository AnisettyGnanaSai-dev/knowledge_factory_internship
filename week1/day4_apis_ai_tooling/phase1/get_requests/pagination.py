import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
    "_page": 1,
    "_limit": 5
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check for HTTP errors
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Unexpected status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
