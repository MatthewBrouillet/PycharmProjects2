import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def current_location():
    """
    >> This function verifies if clicking the current location button on the MAP
    >> of the SERP page.
    """
    # Locating the map
    map = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map

    # Locating the current location button
    current_location = My.search_clickable_webelement(map, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[2]/a")
    assert current_location
    current_location.click()


def testing_current_location():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link)
    current_location()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link)
    current_location()
    driver.quit()
