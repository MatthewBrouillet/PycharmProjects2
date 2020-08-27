import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def in_map_listing_card():
    """
    >> This function verifies if the "Merchant Card", when clicked, leads to the Merchant page
    """
    # Locating the entire search result container (map)
    map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map_results

    # Locating the individual search results
    merchant_card = My.search_presence_webelement(
        map_results, By.XPATH, "//*[@id='ypgBody']/div[2]/div[3]/div[2]/div[2]/div")
    assert merchant_card

    driver.implicitly_wait(5)

    # Locating link to merchant page
    link_to_merchant_page = My.search_clickable_webelement(
        merchant_card, By.XPATH,
        "//*[@id='ypgBody']/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/a")
    assert link_to_merchant_page
    link_to_merchant_page.click()


def test_in_map_listing_card():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    in_map_listing_card()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    in_map_listing_card()
    driver.quit()
