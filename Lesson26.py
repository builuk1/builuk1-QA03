import os
import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')

driver = webdriver.Firefox(service=driver_path_firefox)
url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'
driver.get(url)
q1_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1_xpath = '//input[@name = "q1"]'
q1 = driver.find_element('xpath',q1_xpath)
q1.send_keys('some')
q9_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
q9_xpath = '//input[@name = "q9" and @value = "a"]'
q9_a = driver.find_element('xpath',q9_xpath)
q9_a.click()
q19_xpath = '//input[@name = "q19" and @value = "a"]'
q19_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
q19_a = driver.find_element('xpath',q19_xpath)
q19_a.click()
time.sleep(3)
q19_a.click()
'/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
'/html/body/div/div/div/main/div[3]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'