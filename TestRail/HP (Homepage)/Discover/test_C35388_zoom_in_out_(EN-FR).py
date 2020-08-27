import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def has_zoom_in_out():
    """
    >> This function verifies if the "+" (Zoom in) button and the "-" (Zoom out) button on the map are functional
    """
    # Locating the entire search result container (map)
    map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map_results

    # Locating zoom-in and zoom-out buttons
    zoom_in_button = My.search_clickable_webelement(
        map_results, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[1]")
    zoom_out_button = My.search_clickable_webelement(
        map_results, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[2]")
    assert zoom_in_button
    assert zoom_out_button
    zoom_in_button.click()
    zoom_out_button.click()


def test_has_zoom_in_out():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    has_zoom_in_out()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    has_zoom_in_out()
    driver.quit()
