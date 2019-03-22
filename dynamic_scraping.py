from bs4 import BeautifulSoup
import requests


resource = requests.get('https://www.google.com')

soup = BeautifulSoup(resource.text, 'lxml')


# Normal scraping
container = soup.find('div')
print(container)
