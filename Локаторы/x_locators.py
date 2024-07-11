from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

sign_in = browser.find_element(By.XPATH, "//button[text()='Sign in']")
start_for_free = browser.find_element(By.XPATH, "//button[text()='Start for free']")
logo_link = browser.find_element(By.XPATH, "//a[@class='nav-link']")
explore = browser.find_element(By.XPATH, "//a[contains(text(), 'Explore')]")
pricing = browser.find_element(
    By.XPATH, "//a[@href='/pricing' and contains(text(), 'Pricing')]"
)
for_business = browser.find_element(
    By.XPATH, "//a[@class='nav-link' and contains(text(), 'For Business')]"
)
main_text = browser.find_element(By.XPATH, "//h1[contains(@class, 'mb-12')]")
courses = browser.find_element(
    By.XPATH, "//a[@href='#courses' and @click-event-target='projects']"
)
projects = browser.find_element(
    By.XPATH, "//a[@href='#projects' and @click-event-part='hero_section']"
)
mousewheel = browser.find_element(By.XPATH, "(//body//span)[1]")
select_button = browser.find_element(By.XPATH, "//h2[@id='projects']")
python_button = browser.find_element(
    By.XPATH, "//a[@href='/tracks?pl=python' and text()='Python']"
)
mark = browser.find_element(By.XPATH, "(//body//span//strong)[1]")
text_card = browser.find_element(By.XPATH, "(//body//div//p)[1]")
jet_brains = browser.find_element(
    By.XPATH, "(//body//div//span[text()='JetBrains Academy'])[1]"
)
