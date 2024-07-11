from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element(By.ID, "userName")
full_name.send_keys("Ilya")
assert full_name.get_attribute("value") == "Ilya"

email = driver.find_element(By.CSS_SELECTOR, "[placeholder='name@example.com']")
email.send_keys("example@ex.ex")
assert email.get_attribute("value") == "example@ex.ex"

current_adress = driver.find_element(
    By.XPATH, "(//div//textarea[contains(@id, 'currentAddress')])[1]"
)
current_adress.send_keys("krasnodar")
assert current_adress.get_attribute("value") == "krasnodar"

permanent_adress = driver.find_element(By.ID, "permanentAddress")
permanent_adress.send_keys("ne krasnodar")
assert permanent_adress.get_attribute("value") == "ne krasnodar"

button_submit = driver.find_element(By.ID, "submit")
button_submit.click()

driver.quit()
