import time
from selenium import webdriver

PROXY = "37.19.220.129:8443"  # Указываем адрес прокси-сервера

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://2ip.ru")  # Проверяем IP-адрес

time.sleep(5)


PROXY = "username:password@37.19.220.129:8443"
