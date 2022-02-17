import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')

driver = webdriver.Firefox(service=driver_path_firefox)
url = 'https://core.telegram.org/'
driver.get(url)
# driver.set_window_position(1600,300)#Для второго монитора расположенного справа
time.sleep(2)
driver.maximize_window()
#HEADLESS БЕЗГОЛОВЫЙ Режим работы без визуального запуска
# driver.set_window_size(300,100)
url = 'https://test.mensa.no/'
driver.get(url)