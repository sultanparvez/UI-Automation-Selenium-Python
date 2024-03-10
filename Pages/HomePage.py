from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Locators.HomePageLocators import HomePageLocators
class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.title_locator = HomePageLocators.title_locator

    def assert_login_successful(self):
        try:
            element = self.driver.find_element(By.CLASS_NAME, self.title_locator)
            assert element is not None, f"Element with class name '{self.title_locator}' not found"
        except NoSuchElementException:
            assert False, f"Element with class name '{self.title_locator}' not found"