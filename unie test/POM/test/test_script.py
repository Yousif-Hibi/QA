import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from selenium.webdriver.common.by import By


class TestPaymentTracking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("C:\\Users\\yoyoh\\OneDrive\\Desktop\\QA  Course\\unie test\\POM\\PaymentTrackingScreenForAdminstrator.html")  # Replace with your HTML file path

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('admin')
        login_page.enter_password('admin')
        login_page.click_login()

        # Assert that payment container is displayed
        payment_page = PaymentPage(self.driver)
        self.assertTrue(payment_page.find_element((By.ID, 'payment-container')).is_displayed())

    def test_login_failure(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('wrong_user')
        login_page.enter_password('wrong_pass')
        login_page.click_login()

        # Assert that error message is displayed
        self.assertEqual(login_page.get_error_message(), "Invalid username or password.")

    def test_update_payment_status(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('admin')
        login_page.enter_password('admin')
        login_page.click_login()

        payment_page = PaymentPage(self.driver)
        initial_status = payment_page.get_status_text(0)
        payment_page.click_update_status(0)
        updated_status = payment_page.get_status_text(0)

        # Assert that the status has changed
        self.assertNotEqual(initial_status, updated_status)

    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('admin')
        login_page.enter_password('admin')
        login_page.click_login()

        payment_page = PaymentPage(self.driver)
        payment_page.click_logout()

        # Assert that login container is displayed again
        self.assertTrue(login_page.find_element((By.ID, 'login-container')).is_displayed())


if __name__ == "__main__":
    unittest.main()
