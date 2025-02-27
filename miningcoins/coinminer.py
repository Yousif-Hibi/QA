
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logs

driver = webdriver.Chrome()
file_path = (
    "file:///C:/Users/yoyoh/OneDrive/Desktop/"
    "QA%20%20Course/miningcoins/Miner.html"
)
driver.get(file_path)
wait = WebDriverWait(driver, 10)


def clickMiningButton():
    coinMiningButton = driver.find_element(
        By.XPATH, "/html/body/div/button[1]")
    coinMiningButton.click()


def updatePlayerCoin():
    time.sleep(2)
    playerCoins = driver.find_element(By.ID, "coin-count")

# test 1


clickMiningButton()
updatePlayerCoin()

# test 2
i = 0
playerCoins = driver.find_element(By.ID, "coin-count")
while int(playerCoins.text) <= 50:
    clickMiningButton()
    updatePlayerCoin()
    i = i+1

coinMiningButton = driver.find_element(By.CLASS_NAME, "upgrade")
coinMiningButton.click()
updateresluts = driver.find_element(By.ID, "mine-result")
if updateresluts.text == "שדרגת את מכונת הכרייה!":
    print("upgrade was successful")

# test 3
saveButton = driver.find_element(By.CLASS_NAME, "save-btn")
saveButton.click()
driver.refresh()
updateresluts = driver.find_element(By.ID, "mine-result")
if updateresluts.text == "מוכן לכרייה...":
    print("refresh was successful")

# test 4
challenge = driver.find_element(By.ID, "challenge")
string = challenge.text
# Using list comprehension and isdigit() method
numbers = [int(word) for word in string.split() if word.isdigit()]
i = 0
playerCoins = driver.find_element(By.ID, "coin-count")
while int(playerCoins.text) <= numbers[0]:
    clickMiningButton()
    updatePlayerCoin()
    i = i+1

time.sleep(2)
NextChallenge = driver.find_element(By.ID, "challenge")
if string != NextChallenge.text:
    print("challenge was successful")

time.sleep(10)
driver.quit()
