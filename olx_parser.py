from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs
import json
from selenium.webdriver.common.action_chains import ActionChains
from transliterate import translit, get_available_language_codes
import requests

# Настройка
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome()




links = []
paths  = []
iteration = 0
paginationList = []
domain = 'https://www.olx.kz'


def getPage(url):
    global iteration
    driver.get(url)
    source_data = driver.page_source
    soup = bs(source_data, 'lxml')
    if iteration < 1:
        iteration_box = soup.find('ul', class_='pagination-list')
        pagination = iteration_box.find_all('a' , class_='css-1mi714g')
        for pagCount in pagination:
            try:
                pagText = pagCount.text
                paginationList.append(pagText)

            except:
                print('not found')
    iteration += 1
    GetLinks(soup)

def GetLinks(soup):
    items = soup.find_all('div', class_='css-19ucd76')
    for link in items:
        link_item = link.find('a', class_='css-1bbgabe')
        links.append(link_item)
    for linkHref in links:
        try:
            href = linkHref.get('href')
            paths.append(href)
        except:
            print('href not found')

    if iteration < int(paginationList[-1]):
        getPage('https://www.olx.kz/d/elektronika/telefony-i-aksesuary/?page=' + str(iteration))
        print('next link')

getPage('https://www.olx.kz/d/elektronika/telefony-i-aksesuary/')
data = {}
for path in paths:
    driver.get(domain+path)
    source_data = driver.page_source
    soup = bs(source_data, 'lxml')
    try:
        user = soup.find('h4').text
        id = soup.find('span', class_='css-9xy3gn-Text eu5v0x0')
        data[path] = {
            "user": user,
            "user_id": id.text
        }
    except:
        print('Что то не так')
print(data)
with open('olx_result.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
driver.quit()

input('press any key')
