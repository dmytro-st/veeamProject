import unittest

import constants.constants as const
import constants.departments as department
import constants.languages as language
from environmentSetUp.environmentSetUp import EnvironmentSetUp
from pageObjects.vacancies import Vacancies
from verifiers.verifier import Verifier


class VeeamVacanciesTest(EnvironmentSetUp):
    def setUp(self):
        self.driver = EnvironmentSetUp.initialize(self)
        self.driver.get(const.BASE_URL)

    def test_amount_of_vacancies(self):
        vacancies_page = Vacancies(self.driver)
        vacancies_page.accept_cookies()
        vacancies_page.department_select(department.RESEARCH_AND_DEVELOPMENT)
        vacancies_page.language_select(language.ENGLISH)
        jobs = vacancies_page.get_amount_of_jobs()
        Verifier.compare_amount(jobs, 3)

    def tearDown(self):
        EnvironmentSetUp.close_driver(self)


if __name__ == "__main__":
    unittest.main()
