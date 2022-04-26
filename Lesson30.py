from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath import home_page

# 1
driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua/ru/productstoorder')
driver.maximize_window()
# 2
home_ru = "//ul[@class='menumain']/li/a[@href='/ru/']"

# home_ru_button = driver.find_element('xpath',home_page.home_ru)
home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_page.home_ru)
    )
)
home_ru_button.click()
product_ru = "//ul[@class='menumain']/li/a[@href='/ru/productstoorder']"
# product_ru_button = driver.find_element('xpath',product_ru_ru)
product_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, product_ru)
    )
)
product_ru_button.click()
logo = '//img[@src="http://yanigen.com.ua/images/logo-2015.png"]'
WebDriverWait(driver, 100).until_not(
    EC.presence_of_element_located(
        (By.XPATH, logo)
    )
)
driver.quit()