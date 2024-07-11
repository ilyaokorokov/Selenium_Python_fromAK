from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/en/us/login")

driver.get_cookie(
    "name"
)  # Вернет куку name или любую другую указанную в качестве аргумента
driver.get_cookies()  # Вернет список словарей, все куки

driver.add_cookie({"name": "Example", "value": "Kukushka"})

driver.delete_cookie("name")
driver.delete_all_cookies()


driver.delete_cookie("Example")
driver.add_cookie({"name": "Example", "value": "More"})
