import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




class SearchEngineTests(unittest.TestCase):

    def setUp(self):
        """Set up the browser and navigate to the test page"""
        self.driver = webdriver.Chrome()
        self.driver.get("C:\\Users\\yoyoh\\OneDrive\\Desktop\\QA  Course\\unie test\\Search engine.html")
        self.driver.maximize_window()
        time.sleep(2)  # Ensure the page is fully loaded



    def test_search_bar(self):
        """Test inputting text into the search bar and clicking search"""
        driver = self.driver
        search_bar = driver.find_element(By.ID, "search-bar")
        search_bar.send_keys("בדיקת חיפוש")
        time.sleep(2)

        search_button = driver.find_element(By.ID, "search-btn")
        search_button.click()
        time.sleep(2)

        # Accept the alert after clicking the search button
        alert = Alert(driver)
        alert.accept()
        time.sleep(2)

    def test_popup_handling(self):
        """Test opening and closing a popup window"""
        driver = self.driver
        popup_button = driver.find_element(By.XPATH, "//button[contains(text(),'פתח חלון קופץ')]")
        popup_button.click()
        time.sleep(2)

        close_popup_button = driver.find_element(By.XPATH, "//div[@id='popup']//button[contains(text(),'סגור')]")
        close_popup_button.click()
        time.sleep(2)

    def test_drag_and_drop(self):
        """Test dragging an item to the drop zone"""
        driver = self.driver
        item = driver.find_element(By.CLASS_NAME, "item-1")
        dropzone = driver.find_element(By.CLASS_NAME, "dropzone-area")

        actions = ActionChains(driver)
        actions.drag_and_drop(item, dropzone).perform()
        time.sleep(2)
        self.assertIn("dropped", dropzone.get_attribute("class"), "Item was not successfully dropped.")

       

    def tearDown(self):
        """Close the browser after each test"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
