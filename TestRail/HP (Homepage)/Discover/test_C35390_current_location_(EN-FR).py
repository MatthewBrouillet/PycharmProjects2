import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def has_current_location():
    """
    >> This function verifies if the "Current Location" button on the map is functional
    """
    # Locating the entire search result container (map)
    map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map_results

    # Locating the current location button
    current_location_button = My.search_clickable_webelement(
        map_results, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[2]/a")
    assert current_location_button
    current_location_button.click()


def test_has_current_location():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    has_current_location()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    has_current_location()
    driver.quit()
