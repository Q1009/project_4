import requests
from bs4 import BeautifulSoup

print("Hello World !")
print("Comment ça va ?")
print("Bien merci et toi ?")
print("Quel âge as-tu ?")

r = requests.get("http://www.example.com")
print(r.status_code)
print(r.content)
