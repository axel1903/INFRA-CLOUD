import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Title:", data["title"])
    print("Body:", data["body"])
else:
    print("Request failed")
