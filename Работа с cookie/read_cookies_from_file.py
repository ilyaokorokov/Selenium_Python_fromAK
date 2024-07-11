import pickle
import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/login")
driver.delete_all_cookies()

# Записываем куки из файла в переменную
cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))

# Добавляем по одной куке из списка
for cookie in cookies:
    driver.add_cookie(cookie)

# Делаем запрос на любую страницу залогиненного пользователя
driver.get("https://www.freeconferencecall.com/profile")

# open(os.getcwd() + "/cookies/cookies.pkl") - указываем путь к файлу с ранее записанными куками.
# “rb” (read binaries) - прочитать данные в бинарном формате.
