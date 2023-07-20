import requests
from bs4 import BeautifulSoup

multiPagesFile = open('MultiPages.txt', 'w')

url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

    
pages = soup.find('ul', class_='pagination')
urls = []
links = soup.find_all('a', class_="page-link")
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_="card-title").text.strip('\n')
        itemPrice = i.find('h5').text
        multiPagesFile.write('%s. Price: %s, Item Name: %s \n' % (count, itemPrice, itemName))
        count += 1

multiPagesFile.close()
