import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout = 5)
    response.text # Check if the request was successful
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}, Body: {post['body']}")
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")