import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Test cooment

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://gittmaker.github.io/python-2022-02-28/index.html")
    return driver


def test_welcome_page_header(driver):
    header = driver.find_element(By.TAG_NAME, "h1").text
    # Then
    assert header == "Welcome"


def test_welcome_page_paragraph(driver):
    header = driver.find_element(By.TAG_NAME, "p").text
    # Then
    assert header == "Welcome to the python training!"
