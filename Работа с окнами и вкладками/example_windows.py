import time
from selenium import webdriver

driver = webdriver.Chrome()

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Шаг 3 - Открытие и переключение на новое окно
driver.switch_to.new_window("window")

# Шаг 4 - Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Шаг 5 - Проверка, что окно переключилось
assert new_window == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)

# Шаг 6 - Открытие страницы в новом окне
driver.get("https://vk.com")

# Шаг 7 - Переключение на старое окно
driver.switch_to.window(old_window)

# Шаг 8 - Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Шаг 9 - Открытие страницы в старом окне
driver.get("https://ya.ru")

# Шаг 10 - Переключение на новое окно
driver.switch_to.window(new_window)

# Шаг 11 - Закрытие нового окна
driver.close()
