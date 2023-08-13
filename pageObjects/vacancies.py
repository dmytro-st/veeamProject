from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from environmentSetUp.environmentSetUp import EnvironmentSetUp


class Vacancies(EnvironmentSetUp):

    def __init__(self, driver):
        self.driver = driver
        self.departments_drop_down = (By.XPATH, "(//*[@id= 'sl'])[1]")
        self.languages_drop_down = (By.XPATH, "(//*[@id= 'sl'])[2]")
        self.cookies = (By.ID, "cookiescript_accept")
        self.displayed_jobs = (By.XPATH, "//*[@class = 'card card-sm card-no-hover']")

    def accept_cookies(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.cookies)).click()

    def departments_drop_down_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.departments_drop_down)).click()

    def select_department(self, department):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[. = '{department}']"))).click()

    def languages_drop_down_click(self):
        # self.driver.find_element(self.languages_drop_down).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.languages_drop_down)).click()

    def language_checkbox_click(self, language):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"// label[. = '{language}']"))).click()

    def language_select(self, language_name):
        self.languages_drop_down_click()
        self.language_checkbox_click(language_name)

    def department_select(self, department_name):
        self.departments_drop_down_click()
        self.select_department(department_name)

    def get_amount_of_jobs(self):
        try:
            elements = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located(self.displayed_jobs)
            )
        finally:
            return len(elements)
