from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find_element(locator).text