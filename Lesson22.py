# Selenium Webdriver
# Settings > + > selenium
# https://www.selenium.dev/downloads/
# https://pypi.org/project/selenium/
# https://github.com/mozilla/geckodriver/releases

# for mac
# EXE_PATH = r'path\to\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
# driver = webdriver.Chrome(executable_path=EXE_PATH)
# driver.get('https://google.com')
import os
import time
from selenium import webdriver

driver_path_chrome = os.getcwd() + '\chromedriver.exe'
driver_path_firefox = os.getcwd() + '\geckodriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path_chrome)
# driver.get('https://chromedriver.chromium.org/downloads')
driver = webdriver.Firefox(executable_path=driver_path_firefox)
driver.maximize_window()
# driver.set_window_size(300,100)
driver.get('https://chromedriver.chromium.org/downloads')
driver.get_screenshot_as_file('downloads.png')
time.sleep(5)
driver.get('https://chromedriver.chromium.org')
driver.get_screenshot_as_file('chromium.png')
time.sleep(5)
driver.quit()#Закрывает браузер вообще
#driver.close()#Закрывает вкладку , или наоборот
