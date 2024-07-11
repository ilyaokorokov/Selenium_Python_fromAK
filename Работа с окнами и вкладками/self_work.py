from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://hyperskill.org/login")

driver.switch_to.new_window("tab")
driver.get("https://www.avito.ru/")

driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru/")

tabs = driver.window_handles

driver.switch_to.window(tabs[0])
print("Title вкладки 1:", driver.title)

driver.switch_to.window(tabs[1])
print("Title вкладки 2:", driver.title)

driver.switch_to.window(tabs[2])
print("Title вкладки 3:", driver.title)

driver.switch_to.window(tabs[0])
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

driver.switch_to.window(tabs[1])
avito_element = driver.find_element(By.TAG_NAME, "a")
avito_element.click()

driver.switch_to.window(tabs[2])
ozon_element = driver.find_element(By.TAG_NAME, "a")
ozon_element.click()

time.sleep(5)
driver.quit()
