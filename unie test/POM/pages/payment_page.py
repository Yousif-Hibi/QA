from selenium.webdriver.common.by import By
from .base_page import BasePage

class PaymentPage(BasePage):
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
    STATUS_CELL = (By.CSS_SELECTOR, 'tr td.status')
    ACTION_BUTTON = (By.CSS_SELECTOR, 'tr td .action-button')

    def click_logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    def get_status_text(self, row):
        return self.find_elements(self.STATUS_CELL)[row].text

    def click_update_status(self, row):
        self.find_elements(self.ACTION_BUTTON)[row].click()