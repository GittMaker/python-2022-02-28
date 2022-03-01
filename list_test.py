import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/")
    return driver


def test_list_elements(driver):
    webelements = driver.find_elements(By.TAG_NAME, "li")
    tool_names = []

    for webelement in webelements:
        tool_names.append(webelement.text)

    assert tool_names == ["Python", "Pip", "Webdriver", "Selenium"]