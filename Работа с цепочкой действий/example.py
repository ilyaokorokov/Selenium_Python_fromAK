import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)  # Создаем обьект ожиданий
action = ActionChains(driver)  # Создаем обьект action


element = driver.find_element(...)
action.click(element).preform()

# двойной клик
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
action.double_click(BUTTON).perform()

# клик правой кнопкой мыши
RС_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
BUTTON = driver.find_element(*RС_BUTTON_LOCATOR)
action.context_click(BUTTON).perform()

# наведение на элемент
STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

action.move_to_element(STEP_1).move_to_element(STEP_2).click(STEP_3).perform()

time.sleep(5)


# пауза в цепочке действий
STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

action.move_to_element(STEP_1).move_to_element(STEP_2).pause(5).click(STEP_3).perform()

time.sleep(5)

# скролл к элементу
SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
action.scroll_to_element(SOME_ELEMENT).perform()  # Используем скролл до элемента

# клик с удержанием
OUTLINE_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
BUTTON = driver.find_element(*OUTLINE_BUTTON_LOCATOR)
action.click_and_hold(BUTTON).perform()

# перетаскивание элемента source - элемент который перетаскивают, таргет - область куда перетаскивают
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")
SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)
wait.until(EC.element_to_be_clickable(SOURCE))
action.drag_and_drop(SOURCE, TARGET).perform()  # Перетаскивание
time.sleep(5)

SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source) # Находим source-элемент
    TARGET = driver.find_element(*target) # Находим target-элемент
    wait.until(EC.element_to_be_clickable(SOURCE)) # Ждем кликабельности source-элемента
    action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскиваем

drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR) # Использование функции


# если нужно зажать кнопку мыши а потом через время отпустить
source = driver.find_element("xpath", "//div[@class='grid__item'][7]") # Что перетаскиваем
target = driver.find_element("xpath", "//div[@class='drop-area__item'][2]") # Куда перетаскиваем

action.click_and_hold(source) \
    .pause(2) \
    .move_to_element(target) \
    .release() \
    .perform()