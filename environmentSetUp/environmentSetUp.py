import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class EnvironmentSetUp(unittest.TestCase):

    def initialize(self):
        global Instance
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Maximize browser window
        chrome_options.add_argument("--disable-infobars")  # Disable info bars
        chrome_options.add_argument("--disable-extensions")  # Disable extensions
        chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
        Instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        Instance.implicitly_wait(5)
        return Instance

    def close_driver(self):
        global Instance
        Instance.close()
        Instance.quit()
