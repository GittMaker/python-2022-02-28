from mimetypes import init
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocationsMainPage:
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
        
    def open(self):
        self.driver.get("http://localhost:8080/")
        return self
    
    
    def click_create_location_link(self):
        create_link = self.driver.find_element(By.ID, "create-location-link")
        create_link.click()
        return self
        
    def click_create_submit_btn(self):
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        submit_btn.click()
        return self
        
    def fill_form(self, name:str = "Home", coords:str = "1,1", interesting_at:str = "", tags:str = ""):
        """Kitölti az űrlapot névvel, koordinátákkal, stb."""
        form = self.driver.find_element(By.ID, "location-form")
        
        location_name = form.find_element(By.ID,"location-name")
        location_name.send_keys(name)
        
        location_coords = form.find_element(By.ID, "location-coords")
        location_coords.send_keys(coords)
        
        location_interesting_at = form.find_element(By.ID, "location-interesting-at")
        location_interesting_at.send_keys(interesting_at)
        
        location_tags = form.find_element(By.ID, "location-tags")
        location_tags.send_keys(tags)
        return self
        
    def assert_text_on_message_panel(self, text):
        message_div = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message-div")))
        assert message_div.text == text
        return self
    
    
    def assert_error_message(self, text):
        msg_div = self.driver.find_element(By.CSS_SELECTOR, ".invalid-feedback:not([hidden='hidden'])")
        assert msg_div.text == text