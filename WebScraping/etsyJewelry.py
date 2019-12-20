import pprint
import requests
from bs4 import BeautifulSoup
pageNum = 1
resultsArray = []

while pageNum < 10:
    URL = 'https://www.etsy.com/search?q=tourmaline+wire+wrap&ref=pagination&page=' + str(pageNum)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_='v2-listing-card__info')
    for result in results:
        money = result.find('span', class_='currency-value')
        resultsArray.append(money.text)
    pageNum += 1
for x in resultsArray:
    print(x)
print(len(resultsArray))
# URL = 'https://www.etsy.com/search?q=tourmaline+wire+wrap&ref=pagination&page='
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find_all(class_='v2-listing-card__info')

# for result in results:
#     money = result.find('span', class_='currency-value')
#     print(money.text)

# print(len(results))