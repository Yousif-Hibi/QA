import time
import pytest
import allure 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up the WebDriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("C:\\Users\\yoyoh\\OneDrive\\Desktop\\QA  "
               "Course\\pytestgoogleSearch\\Search engine.html")
    yield driver
    driver.quit()


# Search Test: Check if the search functionality works correctly

@pytest.mark.parametrize("search_query, expected_alert", [
    ("", "לא ניתן לבצע חיפוש ללא הזנת טקסט!"),
    ("פריט 1", "אתה מחפש: פריט 1"),
    ("פריט 2", "אתה מחפש: פריט 2"),
])
@allure.feature("Search Functionality")
@allure.story("Validate Search Alerts")
# Test  search engine
def test_search_engine(driver, search_query, expected_alert):

    # Find the search box and enter a query
    search_box = driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load (you can increase the sleep if needed)
    time.sleep(3)

    search_button = driver.find_element(By.ID, "search-btn")
    search_button.click()

    alert = driver.switch_to.alert

    # Get the text of the alert
    alert_text = alert.text

    # Verify the alert text
    assert alert_text == expected_alert

    # Accept the alert (click OK)
    alert.accept()

    time.sleep(3)

@allure.feature("Popup Functionality")
@allure.story("Verify Popup Visibility and Behavior")
def test_open_popup(driver):
    popup_button = driver.find_element(By.XPATH, "/html/body/div[1]/button[2]")
    popup_button.click()

    # Wait briefly for the popup to appear
    time.sleep(1)

    # Verify the popup is visible
    popup_Box = driver.find_element(By.ID, "popup")
    assert popup_Box.is_displayed()

    popup_heading = popup_Box.find_element(By.TAG_NAME, "h3").text
    assert popup_heading == "זהו חלון קופץ!"

    # Close the popup
    close_button = popup_Box.find_element(By.XPATH,
                                          "//*[@id=\"popup\"]/button")
    close_button.click()

    time.sleep(1)
    assert not popup_Box.is_displayed()
    time.sleep(3)

@allure.feature("Drag and Drop Functionality")
@allure.story("Verify Drag and Drop Behavior")
def test_drag_and_drop(driver):
    # Find the draggable item and drop zone
    draggable_item = driver.find_element(By.XPATH,
                                         "/html/body/table/tbody/tr[1]")
    drop_zone = driver.find_element(By.CLASS_NAME, "dropzone-area")

    # Perform the drag-and-drop action
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(draggable_item, drop_zone).perform()

    # Wait briefly for the drop action to complete
    time.sleep(1)

    # Verify that the item has been dropped into the drop zone
    assert "פריט 1" in drop_zone.text
    time.sleep(3)
