import time
from selenium import webdriver

driver = webdriver.Chrome()

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)

# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows))  # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print(
    "Индекс: ", windows.index(current_tab)
)  # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)

# Шаг 6 - Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"


driver.get("https://hyperskill.org/login")
main_tab = driver.current_window_handle
# Пробуем кликнуть на элемент, который находиться на новой вкладке
START_FOR_FREE_BUTTON = ("xpath", "(//a[text()='Start for Free'])[1]")
driver.find_element(*START_FOR_FREE_BUTTON).click()
list_of_tabs = (
    driver.window_handles
)  # Пример списка ['CDwindow-0DE2EBAE188B1D6CDFAD2DEFF8A1E552', 'CDwindow-A0009183FCA5A328C2DBF38E3E812231']
driver.switch_to.window(
    list_of_tabs[1]
)  # Подставит дескриптор по индексу 1, т.е второй элемент списка
second_tab = (
    driver.current_window_handle
)  # Запишем дескриптор вкладки, на которую переключились выше
assert second_tab != main_tab, "Ошибка переключения между вкладками"
# Пробуем кликнуть на элемент, который находиться на новой вкладке
START_FOR_FREE_BUTTON = ("xpath", "(//a[text()='Start for Free'])[1]")
driver.find_element(*START_FOR_FREE_BUTTON).click()
