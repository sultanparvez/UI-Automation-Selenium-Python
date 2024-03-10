import time
import unittest
# import HtmlTestRunner

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
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Reports))