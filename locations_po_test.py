from LocationsMainPage import LocationsMainPage


def test_create(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form("Home Sweet home", "47.89,19.04")
    page.click_create_submit_btn()
    page.assert_text_on_message_panel("Location has been created")    


def test_empty_name(driver):
    page = LocationsMainPage(driver)
    page.open() \
        .click_create_location_link() \
        .fill_form("") \
        .click_create_submit_btn() \
        .assert_error_message("Can not be empty name!")
    
def test_empty_coords(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form(coords="")
    page.click_create_submit_btn()
    page.assert_error_message("Invalid format!")