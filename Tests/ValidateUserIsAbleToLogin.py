import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
import unittest
import HtmlTestRunner

from selenium import webdriver

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

username = "standard_user"
password = "secret_sauce"


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.saucedemo.com/")

    def test_login_validation(self):
        driver = self.driver
        login = LoginPage(driver)
        homepage = HomePage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        homepage.assert_login_successful()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
    # # Get the directory of the current script
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # # Define the directory for the reports relative to the script directory
    # reports_dir = os.path.join(script_dir, 'Reports')
    # # Run unittest with HtmlTestRunner, specifying the output directory
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reports_dir))
