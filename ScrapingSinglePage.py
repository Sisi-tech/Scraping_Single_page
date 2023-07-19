from bs4 import BeautifulSoup
import requests

singlePageContent = open("SinglePageContent.txt", 'w')
url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
count = 1

for i in items:
    itemName = i.find('h4', class_="card-title").text.strip('\n')
    itemPrice = i.find('h5').text
    singlePageContent.write('%s. Price: %s, Item Name: %s \n' % (count, itemPrice, itemName))
    count += 1


singlePageContent.close()