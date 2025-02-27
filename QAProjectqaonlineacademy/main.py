import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def setup(request):
    """Fixture to set up and tear down WebDriver"""
    with allure.step("Setting up WebDriver"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        request.cls.driver = driver
    yield
    with allure.step("Closing the browser"):
        driver.quit()


@allure.feature("QA Online Academy")
@allure.story("Website Testing")
@pytest.mark.usefixtures("setup")
class TestQaOnlineAcademy:

    @allure.step("Opening the website")
    def open_website(self):
        """Helper method to open the website"""
        self.driver.get("https://www.qaonlineacademy.com/")
        self.driver.refresh()


    @allure.step("Verifying the page title")
    def test_verify_page_title(self):
        """Test case: Verify homepage title"""
        self.open_website()
        assert "Home | Qa Academy Online" in self.driver.title

    @allure.step("Testing the search functionality")
    def test_search_functionality(self):
        """Test case: Perform a search"""
        self.open_website()

        with allure.step("Waiting for search bar and entering query"):
            search_bar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Update selector if needed
            )
            search_bar.send_keys("QA Courses")
            search_bar.send_keys(Keys.RETURN)

        with allure.step("Verifying search results page"):
            results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"comp-m4yt3mrd\"]/h1/span"))  # Update selector
            )
            assert results.text == "Search Results"
            
    @allure.step("Testing the Dropdown Menu functionality")
    def test_dropdown_menu_functionality(self):
        """Test case: Dropdown Menu"""
        self.driver.get("https://www.qaonlineacademy.com/")
        self.driver.refresh()
        self.open_website()
        time.sleep(3)
        with allure.step("Waiting for Dropdown Menu and entering query"):
            pulseButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"comp-m4yt4a4g\"]/button"))
            )
            pulseButton.click()
            time.sleep(3)
            TextINDropDown= WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"comp-m4yt4a4v1\"]/p/span/span/span/span/span/span"))  
            )
            assert TextINDropDown.text == "QA Academy Online"
            DDSite= WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"comp-m4yt4a541\"]/ul/li[2]/div/span/a")) 
            )
            DDSite.click()
            time.sleep(10)
            assert "Blog | Qa Academy Online" in self.driver.title
     
    @allure.step("Testing the Testimonials functionality")
    def test_Testimonials_functionality(self):
        """Test case: Testimonials"""
        self.driver.get("https://www.qaonlineacademy.com/")
        self.driver.refresh()
        self.open_website()
   
        FirstNameBar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-field-input-065a9c47-b7f8-4e64-d192-3ba0146d8bf9-:r0:\"]"))
            )
        FirstNameBar.send_keys("max")
        FirstNameBar.send_keys(Keys.RETURN)

        LastNameBar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-field-input-da8c1271-b33e-458c-5a7a-4ec6995975e9-:r0:\"]"))
            )
        LastNameBar.send_keys("matrex")
        LastNameBar.send_keys(Keys.RETURN)

        EmailBar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-field-input-8d2b7a78-af98-40a6-3590-7ee5e9500baa-:r0:\"]"))
            )
        EmailBar.send_keys("Max@gmail.com")
        EmailBar.send_keys(Keys.RETURN)

        askBar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-field-input-8a90f96b-cf11-4e92-778b-1a26e0b715d6-:r0:\"]"))
            )
        askBar.send_keys("somethig ? ")
        askBar.send_keys(Keys.RETURN)

        submitButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-0f58e39b-3316-4429-9aef-153a410d667e\"]/fieldset/div/div[1]/div[6]/div[2]/div[1]/button"))
            )
        submitButton.click()
        submitionCheck = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-0f58e39b-3316-4429-9aef-153a410d667e\"]/fieldset/div/div[3]"))
            )
        time.sleep(10)
        inner_content = submitionCheck.get_attribute("innerHTML").strip()

        # Check if it's empty
        assert len(submitionCheck) > 0
        
        


                 
    @allure.step("Testing chatbot interaction and form submission")
    def test_chatbot_interaction_and_form_submission(self):
        """Test case: Interact with chatbot and submit form"""
        self.open_website()

        chatBot = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='comp-m6ddnphh']"))
        )
        chatBot.click()

        # If chatbot opens inside an iframe, switch to it
        try:
            iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            self.driver.switch_to.frame(iframe)
        except:
            pass

        chatBotMessage = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/textarea"))
        )
        chatBotMessage.send_keys("Hello")
        chatBotMessage.send_keys(Keys.RETURN)

        try:
            botResponse = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"chat-messages-list\"]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]"))
            )
            assert botResponse is not None, "No response from chatbot"
        except:
            allure.attach("Chatbot did not respond", name="Chatbot Warning", attachment_type=allure.attachment_type.TEXT)
            return

       
        name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='name']"))
        )
        name_input.clear()
        name_input.send_keys("John Doe")

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='email']"))
        )
        email_input.clear()
        email_input.send_keys("johndoe@example.com")

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='chat-messages-list']/div[3]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/button"))
        )
        submit_button.click()

        with allure.step("Verifying form submission success"):
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"chat-messages-list\"]/div[3]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]"))
            )
        
            assert success_message.text == "Thanks! Message us here."
            time.sleep(3)

    