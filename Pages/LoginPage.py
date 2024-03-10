from selenium.webdriver.common.by import By
from Locators.LoginPageLocators import LoginPageLocators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, LoginPageLocators.username_field_locator).clear()
        self.driver.find_element(By.XPATH, LoginPageLocators.username_field_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, LoginPageLocators.password_field_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, LoginPageLocators.login_button_locator).click()
