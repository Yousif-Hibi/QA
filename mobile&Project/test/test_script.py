import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_objects import FormPage, TablePage, DragDropPage  # Import the POM classes


class WebPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver
        cls.driver = webdriver.Chrome()
        cls.driver.get("C:\\Users\\yoyoh\\OneDrive\\Desktop\\QA  Course\\mobile&Project\\Mobile & Web Project.Html")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_form_submission(self):
        """Test filling and submitting a form"""
        form_page = FormPage(self.driver)
        username = "Test User"
        email = "testuser@example.com"
        role = "tester"
        form_page.fill_form(username, email, role)

        # Assert that form submission was successful
        success_message = self.driver.find_element(By.ID, "successMessage").text
        self.assertEqual(success_message, "Form submitted successfully", "Form submission failed!")

    def test_table_data(self):
        """Test fetching and validating table data"""
        table_page = TablePage(self.driver)
        data = table_page.get_table_data()

        # Assert the table is not empty
        self.assertGreater(len(data), 0, "Table data is empty!")

        # Log table data for debugging
        print("Table Data:", data)

    def test_drag_and_drop(self):
        """Test drag and drop functionality"""
        drag_drop_page = DragDropPage(self.driver)

        # Perform drag and drop action
        drag_drop_page.perform_drag_and_drop(0)  # Drag the first draggable item

        # Assert that the item was successfully dropped
        drop_zone = self.driver.find_element(By.ID, "dropZone")
        dropped_text = drop_zone.text
        self.assertIn("Dropped!", dropped_text, "Drag and drop failed!")


if __name__ == "__main__":
    unittest.main()
