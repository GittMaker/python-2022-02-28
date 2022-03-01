import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/")
    return driver


def test_list_elements(driver:webdriver.Chrome):
    webelements = driver.find_elements(By.TAG_NAME, "li")
    tool_names = []

    for webelement in webelements:
        tool_names.append(webelement.text)

    assert tool_names == ["Python", "Pip", "Webdriver", "Selenium"]

def test_table_cells(driver:webdriver.Chrome):
    elements = driver.find_elements(By.CLASS_NAME, "price")
    prices = []
    for element in elements:
        prices.append(int(element.text))
    assert prices == [100, 400, 150]

def test_checkbox(driver:webdriver.Chrome):
    checkbox = driver.find_element(By.NAME, "accept-licence")
    checkbox.click()
    print("End")

def test_select(driver:webdriver.Chrome):
    select = Select(driver.find_element(By.NAME, "car-types"))
    select.select_by_value("opel")
    print("END")
