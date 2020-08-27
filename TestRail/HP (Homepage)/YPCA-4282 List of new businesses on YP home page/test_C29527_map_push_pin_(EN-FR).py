import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def map_push_pin():
    """
    >> This function verifies if the "Merchant Pins" on the map are clickable
    """
    count = 1

    # Locating the entire search result container (map)
    map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
    assert map_results
    assert map_results.is_displayed()

    # Locating the individual search results
    containers = My.search_presence_webelements(map_results, By.XPATH, "//div//div[4]")
    assert containers

    # Looping through every gas station
    for i in containers:
        # Verifying if the merchant link is located on the map and if it is clickable
        merchant_pin = My.search_clickable_webelement(
            i, By.XPATH, "//*[@id='ypgmap']/div[1]/div[4]/div[" + str(count) + "]/div")
        assert merchant_pin

        try:
            webdriver.ActionChains(driver).move_to_element(merchant_pin).click(merchant_pin).perform()
        except:
            return

        count += 1


def testing_map_push_pin():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    map_push_pin()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    map_push_pin()
    driver.quit()
