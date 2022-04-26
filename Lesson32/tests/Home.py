from Lesson32 import config
from Lesson32.XPATH import Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def get(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def change_language_ua(self):
        product_ua_button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, Home.ua_language)
            )
        )
        product_ua_button.click()

    def change_language_ru(self):
        product_ru_button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, Home.ru_language)
            )
        )
        product_ru_button.click()


racoon = BasePage(config.url)
racoon.get()
racoon.change_language_ua()
racoon.change_language_ru()