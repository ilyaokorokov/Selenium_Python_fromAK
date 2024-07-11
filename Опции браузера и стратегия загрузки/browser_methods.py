from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--incognito")
# options.add_argument("----ignore-certificate-errors")
# options.add_argument("----window-size=X,Y")
# options.add_argument("----disable-cache")

# options.page_load_strategy = 'normal'
# options.page_load_strategy = 'eager'
# options.page_load_strategy = 'none'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://ya.ru")
