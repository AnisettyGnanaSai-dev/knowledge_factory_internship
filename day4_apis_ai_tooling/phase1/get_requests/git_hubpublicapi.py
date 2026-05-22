import requests

url = "https://api.github.com/users/octocat"

try:
    response = requests.get(url, timeout=5)
    response.text
    if response.status_code == 200:
        user_data = response.json()
        print(f"Username: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Public Repositories: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
        print(f"Profile URL: {user_data['html_url']}")
    else:
        print(f"Failed to retrieve user data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")