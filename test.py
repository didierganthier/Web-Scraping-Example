import requests
from bs4 import BeautifulSoup
import time

"""
links = []

for i in range(26):
    url = 'http://example.webscraping.com/places/default/index/' + str(i)
    response = requests.get(url)
    print(response)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        tds = soup.findAll('td')
        for td in tds:
            a = td.find('a')
            link = a['href']
            links.append(url + link)
        time.sleep(3)    
print(len(links))

with open('urls.txt', 'w') as file:
     for link in links:
         file.write(links + '\n')

with open('urls.txt', 'r') as file:
    for row in file:
        print(row)
"""
