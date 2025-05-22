import requests
from bs4 import BeautifulSoup

print("Hello World !")

r = requests.get("http://www.example.com")
print(r.status_code)
print(r.content)
