from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

driver.get("https://demoqa.com/upload-download")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_to_be_loaded.txt"
file_path = os.path.join(current_dir, file_name)

upload_file_field = driver.find_element(By.XPATH, "//input[@id='uploadFile']")

upload_file_field.send_keys(file_path)

time.sleep(5)

driver.quit()
