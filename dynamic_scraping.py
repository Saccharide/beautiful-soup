from bs4 import BeautifulSoup
import requests
import re

resource = requests.get('http://thingsthataresmart.wiki/index.php?title=Category:Unpublished_SmartApps')
soup = BeautifulSoup(resource.text, 'lxml')

# Normal scraping
container = soup.find('div')

# https://github.com/search?l=Groovy&p=1&q=smartthings&type=Repositories
print(container)
hmenu = container.find_all('div','hmenu')
print(hmenu)
