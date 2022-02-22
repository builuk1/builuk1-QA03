import os
import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')

driver = webdriver.Firefox(service=driver_path_firefox)
url = 'https://dumskaya.net/'
driver.get(url)

enter_xpath = '//a[@id="pp"]'
enter_button = driver.find_element('xpath',enter_xpath)
enter_button.click()
reg_xpath = '//a[@href="/register/"]'
reg_button = driver.find_element('xpath',reg_xpath)
reg_button.click()
email = 'andrii.builuk4@gmail.com'
email_xpath = '//input[@name="email"]'
email_entry = driver.find_element('xpath',email_xpath)
email_entry.send_keys(email)
name = 'andrii42'
name_xpath = '//input[@name="nick"]'
name_entry = driver.find_element('xpath',name_xpath)
name_entry.send_keys(name)
password = 'andrii421'
password_xpath = '//input[@name="password1"]'#//input[@type="password"]/following::input[@type="password"]
password_entry = driver.find_element('xpath',password_xpath)
password_entry.send_keys(password)
password_c = 'andrii42'
password_c_xpath = '//input[@name="password2"]'#//input[@type="password"]/following::input[@type="password"]/following::input[@type="password"]
password_c_entry = driver.find_element('xpath',password_c_xpath)
password_c_entry.send_keys(password_c)
gender_xpath = '//input[@name="gender" and @value="m"]'
gender_radio = driver.find_element('xpath',gender_xpath)
gender_radio.click()
finish_xpath = '//input[@value="Зарегистрироваться"]'
finish_b = driver.find_element('xpath',finish_xpath)
finish_b.click()