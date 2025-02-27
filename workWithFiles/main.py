from selenium import    webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"C:\Users\yoyoh\OneDrive\Desktop\QA  Course\workWithFiles\index.html")

username = driver.find_element(By.ID,"username")
username.send_keys("test")

password = driver.find_element(By.ID, "password")
password.send_keys("password")

email = driver.find_element(By.ID, "email")
email.send_keys("test@gmail.com")
time.sleep(3)
submit = driver .find_element(By.XPATH, "//*[@id=\"signup-form\"]/button")
submit.click()

time.sleep(3)

downloadButton = driver.find_element(By.XPATH, "/html/body/button[2]")
downloadButton.click()
time.sleep(3)

FileSearch = driver.find_element(By.ID, "file-upload")
FileSearch.send_keys(r"C:\Users\yoyoh\Downloads\example.txt")
Text = FileSearch.get_attribute("value")
print(f"Text : '{Text}'")
try:
    assert Text == 'C:\\fakepath\\example.txt'
    print("assert successful")
except AssertionError:
    print("assert failed")


UploadButton = driver.find_element(By.XPATH, "/html/body/button[1]")
UploadButton.click()
time.sleep(3)
alert = driver.switch_to.alert
print(f"Actual Alert Text: '{alert.text}'")
alert.accept()

time.sleep(3)

driver.quit()
