from selenium import webdriver
import time
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")

driver.find_element(*MULTISELECT).send_keys("Gre")

assert (
    driver.find_element(*MULTISELECT).get_attribute("value") == "Gre"
), "Текст не введен"

driver.find_element(*MULTISELECT).send_keys(Keys.TAB)




driver.find_element(*MULTISELECT).send_keys("Bla")

assert driver.find_element(*MULTISELECT).get_attribute("value") == "Bla", "Текст не введен"

driver.find_element(*MULTISELECT).send_keys(Keys.ENTER)