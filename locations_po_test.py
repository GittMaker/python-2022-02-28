from LocationsMainPage import LocationsMainPage
import requests
import mariadb

def test_create(driver):
    #API hívások, ezt jobb külön fájlba tenni
    # requests.delete("http://localhost:8080/api/locations")
    
    #SQL
    conn = mariadb.connect(user="locations", password="locations", host="localhost", database="locations")
    cur = conn.cursor()
    cur.execute("delete from location")
    conn.commit()
    conn.close()
    
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
    #érdemes áthozni ide az assert-eket, hogy hiba esetén kiírja az assertion error részleteit 
    
    
def test_big_data(driver):
    page = LocationsMainPage(driver)
    page.open()
    
    with open('MOCK_DATA.csv', encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(',')
            page.click_create_location_link()
            page.fill_form(parts[0], parts[1]+","+parts[2])
            page.click_create_submit_btn()
    
