from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pickle
import time

driver = webdriver.Chrome()
# driver.get("https://ya.ru")

# driver.add_cookie({"name": "username", "value": "user123"})
# cookie = driver.get_cookie("username")
# assert cookie["value"] == "user123"
# print(cookie["value"])

# driver.add_cookie({"name": "yandex_login", "value": "support@bronirui-online.ru"})
# cookie = driver.get_cookie("yandex_login")
# print(cookie)
# assert cookie["value"] == "support@bronirui-online.ru"
# driver.delete_cookie("yandex_login")
# driver.refresh()
# deleted_cookie = driver.get_cookie("yandex_login")
# print(deleted_cookie)
# assert deleted_cookie is None

driver.get("https://www.ozon.ru/")
driver.implicitly_wait(20)
driver.maximize_window()
search_field = driver.find_element(By.XPATH, "//input[@placeholder='Искать на Ozon']")
search_field.click()
search_field.send_keys("Python")

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

add_to_cart_buttons = driver.find_elements(By.XPATH, ".//button[.//div[text()='Завтра']]")
for button in add_to_cart_buttons:
    button.click()

go_to_cart_button = driver.find_element(By.XPATH, "//a[@href='/cart']")
go_to_cart_button.click()

cart_counter = driver.find_element(By.XPATH, "//div[@data-widget='header']//div//div[2]")
print(cart_counter.text)
# assert cart_counter.text == "6"

pickle.dump(driver.get_cookies(), open(os.getcwd() + "cookies.pkl", "wb"))

driver.delete_all_cookies()
driver.refresh()
# assert cart_counter is None

cookies = pickle.load(open(os.getcwd()+"cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

# assert cart_counter.text == "6"

# main_page_cart_counter = driver.find_element(By.XPATH, "//div[@data-widget='headerIcon']//div[3]")
# assert main_page_cart_counter.text is None

driver.quit()