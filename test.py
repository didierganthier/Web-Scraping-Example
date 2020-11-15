import requests
from bs4 import BeautifulSoup
import time

'''
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
            links.append("http://example.webscraping.com" + link)
        time.sleep(3)    
print(len(links))

with open('urls.txt', 'w') as file:
     for link in links:
         file.write(link + '\n')
'''

with open('urls.txt', 'r') as file:
    for row in file:
        url = row.strip()
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, features="html.parser")
            country = soup.find('tr', {'id': 'places_country__row'}).find('td', {'class': 'w2p_fw'})
            pop = soup.find('tr', {'id': 'places_population__row'}).find('td', {'class': 'w2p_fw'})
            print('Country: ' + country.text + ', Population: ' + pop.text)
        time.sleep(3)   


 




   