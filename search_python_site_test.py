from urllib.parse import urljoin
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

#pytest.ini-ben definiáltuk a markereket
#pytest -m "marker expression"
#pl.: pytest -m "not slow"
#pl.: pytest -m "slow and basic"
@pytest.mark.fn_search
@pytest.mark.basic
def test_search_pep(driver: WebDriver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "id-search-field").send_keys("pep")
    driver.find_element(By.ID, "submit").click()
    
    first_link = driver.find_element(By.CSS_SELECTOR, "#content > div > section > form > ul > li:nth-child(1) > h3 > a").text
    assert "pep" in first_link.lower()


def test_about(driver: WebDriver, base_url):
    driver.get(urljoin(base_url, "/about/"))
    #driver.find_element(By.LINK_TEXT, "About").click()
    title = driver.title
    assert 'about' in title.lower()
