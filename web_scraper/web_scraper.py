import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"

response = requests.get(url)
content = response.content
print(content)