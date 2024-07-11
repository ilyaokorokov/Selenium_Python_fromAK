from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

iframe_volunteer = driver.find_element(By.XPATH, "//iframe")
driver.switch_to.frame(iframe_volunteer)

first_name_field = driver.find_element(By.XPATH, "//input[@name='RESULT_TextField-1']")
first_name_field.send_keys("Alexey")

driver.switch_to.default_content()  # Переключение с iframe обратно на страницу
