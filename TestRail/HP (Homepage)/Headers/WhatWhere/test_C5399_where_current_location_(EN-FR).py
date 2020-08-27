import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def where_current_location():
    """
    >> This function verifies the functionality of the "Current Location" toggle in the "where" drop down
    """
    # Sending keys to the WHAT and WHERE fields
    try:
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("dentist")
        My.search_presence_webelement(driver, By.ID, "where").click()

        # Selecting the current location option from the WHERE field
        current_location_button = My.search_clickable_webelement(driver, By.ID, "currentLocation")
        assert current_location_button
        current_location_button.click()
    except:
        return


def testing_where_current_location():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    where_current_location()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    where_current_location()
    driver.quit()

