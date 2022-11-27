import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent


user = fake_useragent.UserAgent().random

headers = {'user-agent': user}

session = requests.Session()

page = int(input('Input page '))
url_input = input('Input URL categories')

for i in  range(1, page+1):
    url = f'{url_input}p-{j}'
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    url = "https://kups.club/"

    all_product = soup.find('div', class_='card-title')
    product_list = all_product.find_all('div', class_='card-text')
    print(all_product)

for i in range(len(product_list)):
    product = product_list[i].find('a', class_='votes list')