import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def view_map():
    """
    >> This function verifies if clicking the View Map on the MAP
    >> of the SERP page redirects you to the close-up version of the map.
    """
    # Locating the map
    map = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map

    # Locating the View Map button
    view_map_button = My.search_clickable_webelement(
        map, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/div[1]/aside/ul/li/a")
    assert view_map_button
    view_map_button.click()

    # Locating the close up map
    map_closeup = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgmap"]')
    assert map_closeup


def testing_view_map():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    view_map()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    view_map()
    driver.quit()
