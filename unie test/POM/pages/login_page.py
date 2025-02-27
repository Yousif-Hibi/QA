from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "new_username_id")  # Update the ID if changed
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    ERROR_MESSAGE = (By.ID, 'error-message')

    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)