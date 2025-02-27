from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# הגדרת הנתיב לדפדפן
driver = webdriver.Chrome()  # ודא שהשימוש ב-ChromeDriver מותקן ופעיל

# פתח את הדף
driver.get("C:\\Users\\yoyoh\\OneDrive\\Desktop\\QA  Course\\unie test\\Search engine.html")
# מצא את הקישור לפי ה-XPath שציינת
#link = driver.find_element(By.XPATH, '//*[@id="tbody"]/tr/td[1]/a')

# לחץ על הקישור
#link.click()

# Maximize Browser
driver.maximize_window()

# 🔹 **בדיקה 1: הכנסת טקסט לחיפוש ולחיצה על כפתור החיפוש**
search_bar = driver.find_element(By.ID, "search-bar")
search_bar.send_keys("בדיקת חיפוש")
#search_bar.send_keys(Keys.RETURN)
time.sleep(2)

search_button = driver.find_element(By.ID, "search-btn")
search_button.click()
# ✅ **סגירת ה-ALERT לאחר לחיצה על כפתור החיפוש**
alert = Alert(driver)
alert.accept()
time.sleep(2)

# 🔹 **בדיקה 2: פתיחת חלון קופץ וסגירתו**
popup_button = driver.find_element(By.XPATH, "//button[contains(text(),'פתח חלון קופץ')]")
popup_button.click()
time.sleep(2)

close_popup_button = driver.find_element(By.XPATH, "//div[@id='popup']//button[contains(text(),'סגור')]")
close_popup_button.click()
time.sleep(2)

# איתור האלמנטים לגרירה ושחרור
source_element = driver.find_element(By.CLASS_NAME, "item-1")  # פריט לגרירה
target_element = driver.find_element(By.CLASS_NAME, "dropzone-area")  # אזור שחרור

# ביצוע גרירה ושחרור
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()
time.sleep(5)


# ✅ **סיום הבדיקה וסגירת הדפדפן**
driver.quit()