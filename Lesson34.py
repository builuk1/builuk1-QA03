from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath import home_page

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# with webdriver.Chrome() as driver:
#     # Open URL
#     driver.get('http://yanigen.com.ua/ru/productstoorder')
#     driver.maximize_window()
#     # Setup wait for later
#     wait = WebDriverWait(driver, 10)
#
#     # Store the ID of the original window
#     original_window = driver.current_window_handle
#
#     # Check we don't have other windows open already
#     assert len(driver.window_handles) == 1
#
#     # Click the link which opens in a new window
#     # driver.find_element(By.XPATH, "//ul[@class='menumain']/li/a[@href='/ru/']").click()
#     driver.switch_to.new_window('tab')
#     driver.get("https://seleniumhq.github.io")
#     # Wait for the new window or tab
#     wait.until(EC.number_of_windows_to_be(2))
#
#     # Loop through until we find a new window handle
#     for window_handle in driver.window_handles:
#         if window_handle != original_window:
#             driver.switch_to.window(window_handle)
#             break
#
#     # Wait for the new tab to finish loading content
#     wait.until(EC.title_is("SeleniumHQ Browser Automation"))
driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua/ru/')
#     driver.maximize_window()
button_xpath = '//td[@class="acysubbuttons"]/input'


button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, button_xpath)
    )
)
button.click()
alert = driver.switch_to.alert
alert.accept()