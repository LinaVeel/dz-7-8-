import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"_limit": 5}

response = requests.get(url, params=params)
posts = response.json()

for i, post in enumerate(posts, start=1):
    print(f"Post {i}: {post['title']}")
    print(post['body'])
    print("-" * 40)
