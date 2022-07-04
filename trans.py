from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs
import json
from selenium.webdriver.common.action_chains import ActionChains
from transliterate import translit, get_available_language_codes
import requests
from selenium.webdriver.chrome.options import Options
# Настройка
options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://www.olx.kz/d/obyavlenie/prodam-lg-ne-dorogo-IDkBalU.html'
driver.get(url)
source_data = driver.page_source
soup = bs(source_data, 'lxml')
user_name = soup.find('h4').text
id = soup.find('span', class_='css-9xy3gn-Text eu5v0x0')

user_id = id.text.replace('ID: ', '')

head = {
    "method": "GET",
    "authorization": "Bearer 6de45b867490304a35b06c9d58edfd5e7e895213",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}





element = driver.find_element(by=By.CSS_SELECTOR, value='#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-dwud4b > div.css-1p8n2mw > div > div > div.css-1saqqt7 > div > button')
element.click()
r = requests.get('https://www.olx.kz/api/v1/offers/' + user_id +'/limited-phones/', headers=head)
x = requests.get('https://www.olx.kz/api/v1/offers/'+ user_id +'/phone-view/', headers=head)
print(r)
print(x)


input('enter')
# https://www.olx.kz/api/v1/offers/304384654/phone-view/