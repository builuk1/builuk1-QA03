import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')