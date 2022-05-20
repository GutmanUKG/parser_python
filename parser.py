from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs
import json
from selenium.webdriver.common.action_chains import ActionChains

# Настройка
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome()
domain = 'http://malinabonita.ru/'
itemLinks = []
count = 0
# Функция гуляет по адресам и передает страницу функции поиска и при привышение счетчика запускает функцию формирования массива
def getProduct(url):
    driver.get(url)
    source_data  = driver.page_source
    soup = bs(source_data, 'lxml')
    global count
    count +=1
    if count < 12:
        links(soup, url)
    else:
        data_result(itemLinks)


# Функция поиска
def links(soup, url):
    if url == 'http://malinabonita.ru/loadCatalogMoreProduct':
        links = soup.find_all('a', href=True)
    else:
        box_list = soup.find('div', {"class": "list"})
        links = box_list.find_all('a', href=True)

    for link in links:
        link = link.get('href')
        itemLinks.append(link)


    getProduct('http://malinabonita.ru/loadCatalogMoreProduct')

data = {}
# Формирование массива
def data_result(links):

    for item in links:
         driver.get(domain + item)
         source_data  = driver.page_source
         soup = bs(source_data, 'lxml')
         title = soup.find('h3').text
         imgBox = soup.find_all('div', class_='preview relative')
         imgs = []
         for img in imgBox:
             hrefImg = img.find('a').get('href')
             imgs.append(domain + hrefImg)
         price = soup.find('div', class_='price').text

         data[title] = {
            "name": title,
            "price": price,
            "img_paths": imgs
         }


getProduct('http://malinabonita.ru/catalog/')




# Запись в файл
with open('./public/result.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

driver.quit()
input('press any key')
