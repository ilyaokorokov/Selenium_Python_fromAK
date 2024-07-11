from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")

# Сам чек-бокс для проверки статуса
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")

# Элемент для клика, чтобы выставить флажок
HOME_BUTTON = ("xpath", "//span[text()='Home']")

# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click() 

# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
print(driver.find_element(*HOME_CHECKBOX).is_selected())



driver.get("https://demoqa.com/selectable")

# Записываем локатор первого чек-бокса
FIRST_CHECKBOX = ("xpath", "(//ul[@id='verticalListContainer']/li)[1]")

# Кликаем на него
driver.find_element(*FIRST_CHECKBOX).click()

# Проверяем, что после клика, к нему добавился класс active
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"