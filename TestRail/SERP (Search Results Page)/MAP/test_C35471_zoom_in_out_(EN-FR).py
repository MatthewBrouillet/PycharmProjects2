import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def zoom_in_out():
    """
    >> This function verifies if clicking the zoom-in and zoom-out buttons on the MAP
    >> of the SERP page.
    """
    # Locating the map
    map = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map

    # Locating the zoom-in button
    zoom_in_button = My.search_clickable_webelement(map, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[1]")
    assert zoom_in_button
    zoom_in_button.click()

    # Locating the zoom-out button
    zoom_out_button = My.search_clickable_webelement(map, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[2]")
    assert zoom_out_button
    zoom_out_button.click()


def test_zoom_in_out():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    zoom_in_out()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    zoom_in_out()
    driver.quit()
