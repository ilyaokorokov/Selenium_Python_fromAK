import pickle
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/en/us/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# Логинимся в аккаунт
driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# driver.get_cookies() - вернут нам все куки.
# open(os.getcwd() + "/cookies/cookies.pkl") - указатель места для записи или чтения.
# “wb” (write binary) - запись в бинарном формате (не заморачивайтесь) главное понимать, что это запись.
