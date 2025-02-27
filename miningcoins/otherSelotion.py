
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# יצירת מופע של הדרייבר
driver = webdriver.Chrome()

# פתיחת דף המשחק
file_path = (
    "file:///C:/Users/yoyoh/OneDrive/Desktop/"
    "QA%20%20Course/miningcoins/Miner.html"
)
driver.get(file_path)


# בדיקת טעינת דף הבית
def test_homepage_loads():
    assert "מכונת כריית מטבעות עם בונוסים ואתגרים" in driver.page_source
    print("הדף נטען בהצלחה!")


# בדיקת כריית מטבעות
def test_mining_coins():
    coin_count_element = driver.find_element(By.ID, "coin-count")
    initial_coins = int(coin_count_element.text)

    # לחיצה על כפתור הכרייה
    mine_button = driver.find_element(By.XPATH, "//button[text()='כרה מטבע']")
    mine_button.click()

    # המתנה עד שהכרייה תושלם
    time.sleep(3)

    # בדיקת כמות המטבעות החדשה
    updated_coins = int(coin_count_element.text)
    assert updated_coins > initial_coins
    print(f"כמות המטבעות השתנתה מ-{initial_coins} ל-{updated_coins}")


# בדיקת שדרוג מכונת כרייה
def test_upgrade_miner():
    # הכריית מספיק מטבעות עבור השדרוג
    coin_count_element = driver.find_element(By.ID, "coin-count")
    while int(coin_count_element.text) < 50:
        driver.find_element(By.XPATH, "//button[text()='כרה מטבע']").click()
        time.sleep(5)

    # לחיצה על כפתור השדרוג
    upgrade_button = driver.find_element(By.XPATH, "//button[text()='שדרג מכונת כרייה (עלות: 50 מטבעות)']")
    upgrade_button.click()

    # המתנה קצרה
    time.sleep(5)

    # בדיקת התוצאה
    result_element = driver.find_element(By.ID, "mine-result")
    assert "שדרגת את מכונת הכרייה" in result_element.text
    print("שדרוג מכונת הכרייה הצליח!")


# בדיקת שמירת המשחק
def test_save_game():
    save_button = driver.find_element(By.XPATH, "//button[text()='שמור משחק']")
    save_button.click()

    # המתנה קצרה
    time.sleep(1)

    # בדיקת תוצאה שמאשרת שמירה
    result_element = driver.find_element(By.ID, "mine-result")
    assert "המשחק נשמר בהצלחה" in result_element.text
    print("המשחק נשמר בהצלחה!")


# הפעלת כל הבדיקות
try:
    test_homepage_loads()
    test_mining_coins()
    test_upgrade_miner()
    test_save_game()
finally:
    driver.quit()  # סגירת הדפדפן בסיום הבדיקות