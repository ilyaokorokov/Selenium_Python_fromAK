from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/status_codes")
driver.maximize_window()

status_200 = driver.find_element(By.XPATH, "(//ul//li//a[text()='200'])[1]")
status_200.click()
WebDriverWait(driver, 10).until(EC.url_contains("https://the-internet.herokuapp.com/status_codes/200"))
driver.back()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//ul//li//a[text()='301'])"))).click()
WebDriverWait(driver, 10).until(EC.url_contains("https://the-internet.herokuapp.com/status_codes/301"))
driver.back()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//ul//li//a[text()='404'])"))).click()
WebDriverWait(driver, 10).until(EC.url_contains("https://the-internet.herokuapp.com/status_codes/404"))
driver.back()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//ul//li//a[text()='500'])"))).click()
WebDriverWait(driver, 10).until(EC.url_contains("https://the-internet.herokuapp.com/status_codes/500"))
driver.back()

driver.quit()
