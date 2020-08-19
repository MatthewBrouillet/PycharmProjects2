import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def has_displayed_map_and_businesses():
    """
    >> This function verifies if the "Discover businesses in your area" map is displayed
    >> and if it displays businesses in area
    """
    count = 1

    # Locating the entire search result container (map)
    map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map_results.is_displayed()

    # Locating the individual search results
    containers = My.search_presence_webelements(map_results, By.XPATH, "//div//div[4]")
    assert containers

    # Looping through every gas station
    for i in containers:
        # Verifying if the merchant link is located on the map and if it is clickable
        merchant_pin = My.search_presence_webelement(
            i, By.XPATH, "//*[@id='ypgmap']/div[1]/div[4]/div[" + str(count) + "]/div")
        if not merchant_pin:
            return
        count += 1


def test_has_displayed_map_and_businesses():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.qa_web_link)
    has_displayed_map_and_businesses()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link)
    has_displayed_map_and_businesses()
    driver.quit()
