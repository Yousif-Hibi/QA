from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def get_driver(headless=False):
    """Initialize and return the WebDriver instance."""
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--log-level=3")  # Suppress logs
    driver = webdriver.Chrome(options=options)
    return driver


def handle_alert(driver):
    """Handle alert pop-ups."""
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()


def register_user(driver, username_text, email, password):
    """Fill out the registration form and submit."""
    driver.find_element(By.ID, "signupName").send_keys(username_text)
    driver.find_element(By.ID, "signupEmail").send_keys(email)
    driver.find_element(By.ID, "signupPassword").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id=\"signup-page\"]/div/button").click()


def login_user(driver, email, password):
    """Fill out the login form and submit."""
    driver.find_element(By.ID, "loginEmail").send_keys(email)
    driver.find_element(By.ID, "loginPassword").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id=\"login-page\"]/div/button").click()


def run_test(headless_mode):
    """Main function to execute registration, login, and screenshot."""
    driver = get_driver(headless=headless_mode)

    driver.get(r"C:\Users\yoyoh\OneDrive\Desktop\QA  Course\FaceAbook\index.html")
    time.sleep(2)  # Wait for page to load
    
    # Register User
    register_user(driver, "test", "test@gmail.com", "password")
    time.sleep(2)  # Wait for alert after registration
    handle_alert(driver)

    # Login User
    login_user(driver, "test@gmail.com", "password")
    time.sleep(2)  # Wait for alert after login
    handle_alert(driver)

    # Take screenshot
    time.sleep(2)  # Wait for page to fully load after login
    screenshot_filename = "screenshot_headless.png" if headless_mode else "screenshot_normal.png"
    driver.save_screenshot(screenshot_filename)

    time.sleep(10)
    driver.quit()


def main():
    """Run tests in both headless and normal modes."""
    # Run with headless mode
    print("Running test in headless mode...")
    run_test(headless_mode=True)

    # Run with normal mode (not headless)
    print("Running test in normal mode...")
    run_test(headless_mode=False)


if __name__ == "__main__":
    main()
