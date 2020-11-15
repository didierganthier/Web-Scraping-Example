import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/'

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    tds = soup.findAll('td')
    [print(str(td) + '\n\n' ) for td in tds]