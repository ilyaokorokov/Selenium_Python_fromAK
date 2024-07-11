from selenium import webdriver

driver = webdriver.Chrome()

driver.switch_to.new_window("tab")  # Открытие новой вкладки и переключение на нее
driver.switch_to.new_window("window")  # Открытие нового окна и переключение на него

driver.get("https://hyperskill.org/login")

# Клик по кнопке, которая открывает новую вкладку
FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
driver.find_element(*FOR_BUSINESS_BUTTON).click()


current_tab = driver.current_window_handle
print(
    current_tab
)  # 'CDwindow-A274A0735C4C3C8C6C69464186962DD0' # Дескриптор окна или вкладки


windows_count = driver.window_handles  # Записываем список открытых окон в переменную
print(
    windows_count
)  # Выводим на экран полученный список ['CDwindow-A274A0735C4C3C8C6C69464186962DD0', 'CDwindow-550185EAFE1335F1C2FF6992BE3420FC', 'CDwindow-7742FF146E8ACBF35FFEB50E685EF409']

windows_count = driver.window_handles  # Записываем список открытых окон в переменную
print(len(windows_count))  # Выводим на экран кол-во открытых окон/вкладок


driver.quit()  # Закрытие сессии, т.е всего браузера
driver.close()  # Закрытие активного окна / вкладки
