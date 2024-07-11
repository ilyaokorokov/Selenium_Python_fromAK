from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/selectable")

grid_btn = driver.find_element(By.ID, "demo-tab-grid")
grid_btn.click()

grid_items = driver.find_elements(By.CSS_SELECTOR, "li.list-group-item")

for element in grid_items:
    if element.text in ("One", "Two"):
        element.click()
        assert "active" in element.get_attribute("class"), "Чек-бокс не выбран"
        element.click()
        assert "active" not in element.get_attribute("class"), "Чек-бокс выбран"

driver.quit()
