import pprint
import requests
from bs4 import BeautifulSoup
resultsArray = []


URL = 'https://offerup.com/search/?q=washer%20and%20dryer'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(page.content)
results = soup.find_all(class_='_109rpto _1anrh0x')
for result in results:
    money = result.find('span', class_='_s3g03e4')
    print(money.text)
    resultsArray.append(money.text)

for x in resultsArray:
    print(x)
print(len(resultsArray))