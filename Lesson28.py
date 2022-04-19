from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua/ru/shop/wallets-purses/neat2-detail')
time.sleep(5)
driver.maximize_window()
driver.get_screenshot_as_file('google.png')

home_ru = "//a[contains(text(),'ГЛАВНАЯ')]"
home2_ru = "//ul[@class='menumain']/li/a[@href='/ru/']"
home_ua = "//a[contains(text(),'ГОЛОВНА')]"
home_en = "//a[contains(text(),'HOME')]"
product = "//a[contains(text(),'ИЗДЕЛИЯ НА ЗАКАЗ')]"

a = '//li[@class="bjqs-prev"]/a[@data-direction="previous"]'
button = driver.find_element('xpath',a)
button.click()
time.sleep(5)
button.click()
time.sleep(2)
while True:
    button.click()
    time.sleep(2)