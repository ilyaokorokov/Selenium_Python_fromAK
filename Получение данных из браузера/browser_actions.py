from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://vk.com")
print(browser.title)

browser.get("https://ya.ru")
print(browser.title)

browser.back()
url = browser.current_url
print(url)
assert url == "https://vk.com/"

browser.forward()
WebDriverWait(browser, 10).until(EC.url_to_be("https://ya.ru/"))
assert (
    browser.current_url == "https://ya.ru/"
), f"Expected 'https://ya.ru/', but got {browser.current_url}"

print(browser.current_url)
browser.quit()
