from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_welcome_page_header():
    # Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Then
    driver.get("https://gittmaker.github.io/python-2022-02-28/index.html")
    header = driver.find_element(By.TAG_NAME, "h1").text
    # Then
    assert header == "Welcome"


def test_welcome_page_paragraph():
    # Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Then
    driver.get("https://gittmaker.github.io/python-2022-02-28/index.html")
    header = driver.find_element(By.TAG_NAME, "p").text
    # Then
    assert header == "Welcome to the python trainig"