from pprint import pprint
import requests
from bs4 import BeautifulSoup
import collections
pageNum = 1
resultsArray = []
Item = collections.namedtuple('Item', [
    'Title',
    'Price',
])
while pageNum < 10:
    URL = 'https://www.etsy.com/search?q=tourmaline+wire+wrap&ref=pagination&page=' + str(pageNum)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_='v2-listing-card__info')
    for result in results:
        header = result.find('h2', class_='text-body')
        money = result.find('span', class_='currency-value')
        res = Item(Title=header.text, Price=money.text)
        resultsArray.append(res)
    pageNum += 1
for x in resultsArray:
    print(x)
pprint(len(resultsArray))
