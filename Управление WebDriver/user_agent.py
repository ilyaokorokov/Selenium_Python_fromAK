from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pytest

# Но что если нужен какой-то конкретный User-agent? Вот готовый список, который постоянно обновляется:

# https://useragents.ru/stable.html - ПК агенты
# https://deviceatlas.com/blog/mobile-browser-user-agent-strings - мобильные агенты


options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

driver.get("https://vk.com") # страница пк версии


options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36")
driver = webdriver.Chrome(options=options)

driver.get("https://vk.com") #страница мобильной версии, т.к. указали мобильный агент