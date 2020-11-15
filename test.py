import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/'

response = requests.get(url)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, features="html.parser")
    tds = soup.findAll('td')
    for td in tds:
        a = td.find('a')
        link = a['href']
        links.append(link)
    print(links)    