from selenium.webdriver import Keys
from selenium import webdriver
import time
import platform

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/key_presses")  # Сайт для работы

KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")  # Поле ввода

driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello World")  # Ввод текста

driver.find_element(*KEY_PRESS_INPUT).send_keys(
    Keys.COMMAND + "A"
)  # Выделение всего текста

driver.find_element(*KEY_PRESS_INPUT).send_keys(
    Keys.BACKSPACE
)  # Удаление выделенного текста


COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")

COPY = driver.find_element(*COPY_LOCATOR)
PASTE = driver.find_element(*PASTE_LOCATOR)

PASTE.send_keys(cmd_ctrl + "A")  # Выделим все внутри поля
time.sleep(2)
PASTE.send_keys(cmd_ctrl + "X")  # Вырежем весь текст
time.sleep(2)
PASTE.send_keys(cmd_ctrl + "V")  # Вставим весь текст


# Чтобы избежать ошибок из-за разницы систем с CONTROL и COMMAND можно написать следующий код, создав универсальную клавишу CMD_CTRL.
os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

driver = webdriver.Chrome()
driver.find_element().send_keys(CMD_CTRL + "A")  # Использование
