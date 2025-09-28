import redis
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

client = redis.Redis(host='localhost', port=6379, db=0)
print(client.ping())

for post in data:
    client.hset(f"user:{post['id']}",
                mapping={
                    "userId": post["userId"],
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })


user = client.hgetall(f"user:{post['id']}")
user = {k.decode(): v.decode() for k, v in user.items()}
print(user)

