# joke request homework
import requests
from random import choice
url = "https://icanhazdadjoke.com/search?term=" + input("Let me tell you a joke! Give me a topic: ")
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()
search_term = data["search_term"]
total = data["total_jokes"]
print(f"I've got 12 jokes about {search_term}. Here's one:")
print(choice(data["results"])["joke"])