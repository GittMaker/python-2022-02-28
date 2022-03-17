import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver(base_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(base_url)
    return driver
