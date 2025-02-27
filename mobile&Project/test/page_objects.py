from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.CSS_SELECTOR, "input[placeholder=\"הכנס שם משתמש\"]")
        self.email_field = (By.CSS_SELECTOR, "input[placeholder=\"הכנס אימייל\"]")
        self.role_dropdown = (By.ID, "drag-drop-section")
        self.submit_button = (By.XPATH, "//*[@id=\"form-section\"]/form/button")

    def fill_form(self, username, email, role):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.role_dropdown).send_keys(role)
        self.driver.find_element(*self.submit_button).click()

class TablePage:
    def __init__(self, driver):
        self.driver = driver
        self.table_rows = (By.CSS_SELECTOR, "table tbody tr")

    def get_table_data(self):
        rows = self.driver.find_elements(*self.table_rows)
        data = [row.text for row in rows]
        return data

class  DragDropPage:
    def __init__(self, driver):
        self.driver = driver
        self.draggable_items = (By.CSS_SELECTOR, ".draggable")
        self.drop_zone = (By.ID, "dropZone")

    def perform_drag_and_drop(self, index):
        items = self.driver.find_elements(*self.draggable_items)
        drop_zone = self.driver.find_element(*self.drop_zone)
        ActionChains(self.driver).drag_and_drop(items[index], drop_zone).perform()
