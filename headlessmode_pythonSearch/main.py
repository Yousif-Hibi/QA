
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options = Options()

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")  # Suppress logs


driver = webdriver.Chrome(options=options)
driver.get("https://www.bing.com/")
time.sleep(2)

searchBar = driver.find_element(By.NAME, "q")
searchBar.send_keys("Python")
time.sleep(2)
searchBar.send_keys(Keys.RETURN)

results = driver.find_elements(By.CSS_SELECTOR, "a h3")
time.sleep(2)
driver.save_screenshot("headless.png")
print(driver.title)
driver.quit()
