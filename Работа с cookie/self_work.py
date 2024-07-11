from selenium import webdriver
import os
import pickle
import time

driver = webdriver.Chrome()
driver.get("https://ya.ru")

driver.add_cookie({"name": "username", "value": "user123"})
cookie = driver.get_cookie("username")
assert cookie["value"] == "user123"
print(cookie)

driver.quit()
