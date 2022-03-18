from turtle import title
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_screenshot(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/docs/messages/index.html")
    
    live_alert_btn = driver.find_element(By.ID, "liveAlertTimeoutBtn")
    live_alert_btn.click()

    message_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert message_div.text == "Nice, you triggered this alert message!"
