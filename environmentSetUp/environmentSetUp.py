from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class EnvironmentSetUp:

    def initialize(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Maximize browser window
        chrome_options.add_argument("--disable-infobars")  # Disable info bars
        chrome_options.add_argument("--disable-extensions")  # Disable extensions
        chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(5)
        return self.driver

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
