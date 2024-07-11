import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0"
)
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown")  # Страница для работы

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))


<select id="dropdown">
    <option value="" disabled="disabled" selected="selected">Please select option</option>
    <option value="1">Option 1</option>
    <option value="2">Option 2</option>
</select>

# по содержимому текста
DROPDOWN.select_by_visible_text("Option 2")
# по индексу
DROPDOWN.select_by_index(2)
# по value
DROPDOWN.select_by_value("2")
print(DROPDOWN.options) # Вернет все элементы


DROPDOWN_LOCATOR = ("xpath", "//select[@id='oldSelectMenu']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR)) 
all_options = DROPDOWN.options # Запишем все элементы выпадающего списка
for option in all_options: # Перебор элементов по тексту 
    time.sleep(1)
    DROPDOWN.select_by_visible_text(option.text)

for option in all_options: # Перебор элементов по индексу 
    time.sleep(1)
    DROPDOWN.select_by_index(all_options.index(option))

for option in all_options: # Перебор элементов по value 
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))