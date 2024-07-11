from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# options = webdriver.ChromeOptions()
# options.add_argument("")

# service = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome()
# driver.implicitly_wait(50)

# driver.get("https://demoqa.com/dynamic-properties")

# after_btn = driver.find_element(By.ID, "visibleAfter")
# after_btn.click()

# wait = WebDriverWait(driver, 30, poll_frequency=1)

# driver - Ну понятное дело, он же ждать то будет)
# 30 (любое число) - это количество секунд, в течение которого драйвер будет ждать выполнения того или иного условия
# poll_frequency=1 - определяет то, как часто делать новый запрос на проверку выполнения ожидаемого условия. В данном случае 1 секунда.

# wait.until(EC.visibility_of_element(("xpath", "//button[@id='login_button']")), message="Кнопка 'Войти' не найдена")

# ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='sbm']")

# wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON)) # Ждем пока кнопка станет кликабельной
# driver.find_element(*ADD_ELEMENT_BUTTON).click()

# driver.quit()



driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")

wait_25_seconds = WebDriverWait(driver, 25)

text_invisible = driver.find_element(By.ID, "deletesuccess")
wait_25_seconds.until(EC.invisibility_of_element_located("deletesuccess"))

text_visible = driver.find_element(By.ID, "delayedText")
wait_25_seconds.until(EC.visibility_of_element_located((By.ID, "delayedText")))

btn_to_click = driver.find_element(By.ID, "timerButton")
wait_25_seconds.until(EC.element_to_be_clickable((By.ID, "timerButton"))).click()

try_btn = driver.find_element(By.XPATH, "//button[text()='Try it']")
attr_from_btn = driver.find_element(By.ID, "myBtn")
text_attr1 = attr_from_btn.get_attribute("disabled")
print(text_attr1)
try_btn.click()
wait_25_seconds.until(EC.text_to_be_present_in_element_attribute((By.ID, "myBtn"), "disabled", ""))
text_attr2 = attr_from_btn.get_attribute("disabled")
print(text_attr2)

assert text_attr2 == "true"

driver.quit()