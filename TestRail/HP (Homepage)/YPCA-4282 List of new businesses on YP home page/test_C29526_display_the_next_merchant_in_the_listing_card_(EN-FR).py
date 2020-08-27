import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def next_merchant_in_listing_card():
    """
    >> This function verifies if the "Next Discovery" toggle on the merchant card, within the map, is functional
    """
    # Locating the entire search result container (map)
    map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map_results

    # Locating the individual search results
    merchant_card = My.search_presence_webelement(
        map_results, By.XPATH, "//*[@id='ypgBody']/div[2]/div[3]/div[2]/div[2]/div")
    assert merchant_card

    # Locating the Next Discovery button on the merchant card
    next_discovery = My.search_clickable_webelement(
        merchant_card, By.XPATH, "//*[@id='ypgBody']/div[2]/div[3]/div[2]/div[2]/div/div[2]/a")
    assert next_discovery
    next_discovery.click()


def test_next_merchant_in_listing_card():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    next_merchant_in_listing_card()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    next_merchant_in_listing_card()
    driver.quit()
