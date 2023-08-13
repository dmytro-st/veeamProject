import unittest

import constants.constants as const
import constants.departments as department
import constants.languages as language
from environmentSetUp.environmentSetUp import EnvironmentSetUp
from pageObjects.vacancies import Vacancies
from verifiers.verifier import Verifier


class VeeamVacanciesTest(EnvironmentSetUp, unittest.TestCase):
    def setUp(self):
        self.initialize()
        self.driver.get(const.BASE_URL)

    def test_amount_of_rd_english_jobs(self):
        vacancies_page = Vacancies(self.driver)
        vacancies_page.accept_cookies()
        vacancies_page.department_select(department.RESEARCH_AND_DEVELOPMENT)
        vacancies_page.language_select(language.ENGLISH)
        jobs = vacancies_page.get_amount_of_jobs()
        Verifier.compare_amount(jobs, 3)

    def test_amount_of_all_german_jobs(self):
        vacancies_page = Vacancies(self.driver)
        vacancies_page.accept_cookies()
        vacancies_page.language_select(language.GERMAN)
        jobs = vacancies_page.get_amount_of_jobs()
        Verifier.compare_amount(jobs, 1)

    def test_amount_of_qa_jobs(self):
        vacancies_page = Vacancies(self.driver)
        vacancies_page.accept_cookies()
        vacancies_page.department_select(department.QUALITY_ASSURANCE)
        jobs = vacancies_page.get_amount_of_jobs()
        Verifier.compare_amount(jobs, 13)

    def tearDown(self):
        self.close_driver()


if __name__ == "__main__":
    unittest.main()
