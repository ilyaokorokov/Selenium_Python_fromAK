from selenium import webdriver
import time
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

SELECT_TITLE = (
    "xpath",
    "//input[@id='react-select-3-input']",
)  # Локатор нашего dropdown

driver.find_element(*SELECT_TITLE).send_keys("Mrs.")  # Вводим текст в dropdown

time.sleep(5)

driver.find_element(*SELECT_TITLE).send_keys(Keys.ENTER)


# Клик напрямую
driver.get("https://demoqa.com/select-menu")
driver.find_element("xpath", "//div[@id='withOptGroup']").click()  # Открываем dropdown
driver.find_element(
    "xpath", "//div[@id='withOptGroup']//div[text()='A root option']"
).click()  # Кликаем на элемент внутри


# Функция для выбора
driver.get("https://demoqa.com/select-menu")
driver.find_element("xpath", "//div[@id='withOptGroup']").click()  # Открываем dropdown
def choose_dropwdown_element_by_text(
    text,
):  # Будем искать элемент внутри dropdown по тексту
    elements = driver.find_elements(
        "xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]"
    )
    for element in elements:
        if text in element.text:
            return element  # Возвращаем нужный элемент из dropdown по тексту


choose_dropwdown_element_by_text(
    "Another root option"
).click()  # Кликаем на выбранный элемент
