from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox.click()

driver.get("http://the-internet.herokuapp.com/checkboxes")

# Обьявляем локаторы
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

# Выполняем клик по первому чек-боксу
driver.find_element(*CHECKBOX_1).click()

# Убеждаемся что первый чек-бокс действительно выставлен
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None

# Выполняем клик по второму чек-боксу
driver.find_element(*CHECKBOX_2).click()

# Убеждаемся что второй чек-бокс действительно не выставлен
assert driver.find_element(*CHECKBOX_2).get_attribute("checked") is None

# Ставим флажок
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"

# Убираем флажок
driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"