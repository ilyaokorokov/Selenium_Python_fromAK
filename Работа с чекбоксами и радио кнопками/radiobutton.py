from selenium import webdriver
from selenium.webdriver.common.by import By

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")



YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']") # Для статуса
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']") # Для взаимодействия

driver.find_element(*YES_RADIO_LABEL).click()

assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка не выбрана"