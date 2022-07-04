from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs
import json
from selenium.webdriver.common.action_chains import ActionChains
from transliterate import translit, get_available_language_codes


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
    if count < 16:
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
         en_name = translit(title,  language_code='ru', reversed=True)
         en_name = en_name.replace(" ", "_")
         en_name = en_name.replace("\"", "_")
         en_name = en_name.replace(",", "")
         imgBox = soup.find_all('div', class_='preview relative')
         description = soup.find('div', class_='description').text
         imgs = []
         for img in imgBox:
             hrefImg = img.find('a').get('href')
             imgs.append(domain + hrefImg)
         price = soup.find('div', class_='price').text

         data[title] = {
            "name": title,
             "en_name": en_name,
            "price": price,
            "img_paths": imgs,
             "description": description
         }


getProduct('http://malinabonita.ru/catalog/')




# Запись в файл
with open('./public/result.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

driver.quit()
input('press any key')
