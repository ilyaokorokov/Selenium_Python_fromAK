import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Импортируем Options

options = Options()
preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "for_download_files")
}
options.add_experimental_option("prefs", preferences)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

driver.get("http://the-internet.herokuapp.com/download")

files = driver.find_elements(By.XPATH, "//a[contains(@href, 'download/')]")
for element in files:
    element.click()

time.sleep(5)

driver.quit()
