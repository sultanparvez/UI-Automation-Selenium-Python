import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

import unittest
import HtmlTestRunner

from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Config.Config import TestData

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.BASE_URL)

    def test_login_validation(self):
        driver = self.driver
        login = LoginPage(driver)
        homepage = HomePage(driver)
        login.enter_username(TestData.username)
        login.enter_password(TestData.password)
        login.click_login()
        homepage.assert_login_successful()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
