import time
import csv
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
options = Options()
# options.add_argument("--headless")  # Uncomment for headless execution
options.add_argument("--disable-gpu")

# Start WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://www.bing.com")

# Wait for the page to load
time.sleep(2)

# Locate search box and perform search
search_box = driver.find_element(By.NAME, "q")
search_term = "Python"
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Get the first 5 search results with title and URL
search_results = []
results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo")[:5]  # Selects search result blocks

for result in results:
    try:
        title_element = result.find_element(By.CSS_SELECTOR, "h2 a")  # Gets the title link
        title = title_element.text
        url = title_element.get_attribute("href")
        search_results.append((search_term, title, url))
    except Exception:
        continue  # Skip if any element is missing

# Save screenshot
screenshot_path = "screenshot.png"
driver.save_screenshot(screenshot_path)

# Save results to CSV
csv_file = "search_results.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Search Term", "Title", "URL"])
    writer.writerows(search_results)

# Save results to Excel using OpenPyXL
excel_file = "search_results.xlsx"
wb = Workbook()
ws = wb.active
ws.append(["Search Term", "Title", "URL"])

for row in search_results:
    ws.append(row)

wb.save(excel_file)

# Close WebDriver
driver.quit()
