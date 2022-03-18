from turtle import title
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# save screenshot
def test_screenshot(driver: WebDriver):
    driver.get("https://www.training360.com/")
    title = driver.title
    
    driver.save_screenshot("img/main.png")
    div = driver.find_element(By.CSS_SELECTOR, "[data-href='/irodai-informatika']")
    cookie_close_btn = driver.find_element(By.CSS_SELECTOR, ".cookie__button")
    
    newsletter_close_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "NewsletterModalCloseButton")))
    newsletter_close_btn.click()
    
    cookie_close_btn.click()
    div.screenshot("img/button.png")
    assert "Informatikai tanfolyamok" in title
