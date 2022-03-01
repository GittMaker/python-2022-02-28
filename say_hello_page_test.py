import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/welcome.html")
    return driver


def test_say_hello_(driver:webdriver.Chrome):
    input_field = driver.find_element(By.ID, "name-input")
    input_field.send_keys("John Doe")
    button = driver.find_element(By.ID, "hello-btn")
    button.click()

    message_paragraph = driver.find_element(By.ID, "message-p")
    assert message_paragraph.text == "Hello John Doe!"
