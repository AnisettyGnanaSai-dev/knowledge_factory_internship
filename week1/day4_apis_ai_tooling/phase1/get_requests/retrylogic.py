import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise an error for HTTP errors
            break  # If successful, exit the retry loop
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    else:
        print("All retry attempts failed.")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}, Body: {post['body']}")
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")