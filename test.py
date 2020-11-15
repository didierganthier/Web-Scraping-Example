import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/'

response = requests.get(url)

if response.ok:
    print(response.text)