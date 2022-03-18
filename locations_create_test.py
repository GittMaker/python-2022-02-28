from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_with_correct_data(driver: WebDriver):
    driver.get("http://localhost:8080/")
    
    numOfRows = len(driver.find_elements(By.CSS_SELECTOR, ".locations-table-tbody tr"))
    
    create_link = driver.find_element(By.ID, "create-location-link")
    create_link.click()
    
    form = driver.find_element(By.ID, "location-form")
    location_name = form.find_element(By.ID,"location-name")
    location_coords = form.find_element(By.ID, "location-coords")
    location_interesting_at = form.find_element(By.ID, "location-interesting-at")
    location_tags = form.find_element(By.ID, "location-tags")
    submit_btn = form.find_element(By.CSS_SELECTOR, "[type='submit']")
    
    location_name.send_keys("Location01")
    location_coords.send_keys("1,1")
    submit_btn.click()
    
    message_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message-div")))
    new_row = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#locations-table-tbody"), "Location01"))

    table_rows = driver.find_elements(By.CSS_SELECTOR, "#locations-table-tbody tr td:nth-child(1)")
    isInTable = False
    for cell in table_rows:
        if int(cell.text) == (numOfRows + 1):
            isInTable = True
    
    assert "Location has been created" in message_div.text and isInTable
    
def test_delete_row(driver: WebDriver):
    driver.get("http://localhost:8080/")

    last_row_location_name = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody tr:last-child td:nth-child(2)").text
    last_row_delete_btn = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody tr:last-child td:nth-child(6) button.btn-danger")
    last_row_delete_btn.click()
    
    delete_btn = driver.find_element(By.CSS_SELECTOR, ".btn-danger[value='Delete location']")
    delete_btn.click()
    
    isInTable = True
    try:
        deleted_row = WebDriverWait(driver, 10).until_not(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#locations-table-tbody tr:last-child td:nth-child(2)"), last_row_location_name))
    finally:
        isInTable = False

    assert isInTable == False