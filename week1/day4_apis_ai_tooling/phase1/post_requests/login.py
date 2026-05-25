import requests

url = "https://reqres.in/api/login"

data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print("Status:", response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")