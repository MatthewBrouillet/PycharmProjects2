import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def travel_options():
    """
    >> This function verifies if the 3 travel options are displayed on the merchant page.
    """
    first_merchant_card = My.search_presence_webelement(
        driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    merchant_name = My.search_clickable_webelement(
        first_merchant_card, By.TAG_NAME, "h3")
    assert merchant_name
    merchant_name.click()

    mini_map = My.search_clickable_webelement(
        driver, By.XPATH, '//*[@id="ypgBody"]/div[3]/div/div[4]/div[2]/div[2]/div[2]/div[2]/ul/li/a')
    assert mini_map
    mini_map.click()

    url = driver.current_url[32:56]
    assert '/merchant/directions/' in url

    current_location_icon = My.search_clickable_webelement(
        driver, By.XPATH, '//*[@id="DRIVING"]/form/div[2]/div[1]/span[3]')
    assert current_location_icon
    current_location_icon.click()

    count = 1
    while count < 4:
        travel_option = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="DRIVING"]/form/div[1]/ul/li[' + str(count) + ']/a')
        if count == 1:
            assert travel_option

        elif count == 2:
            assert travel_option

        else:
            assert travel_option

        count += 1

    # Locating the FR language toggle
    fr_toggle = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[2]/a")
    assert fr_toggle
    fr_toggle.click()

    current_location_icon = My.search_clickable_webelement(
        driver, By.XPATH, '//*[@id="DRIVING"]/form/div[2]/div[1]/span[3]')
    assert current_location_icon
    current_location_icon.click()

    count = 1
    while count < 4:
        travel_option = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="DRIVING"]/form/div[1]/ul/li[' + str(count) + ']/a')
        if count == 1:
            assert travel_option

        elif count == 2:
            assert travel_option

        else:
            assert travel_option

        count += 1


def testing_travel_options():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    travel_options()
    driver.quit()
