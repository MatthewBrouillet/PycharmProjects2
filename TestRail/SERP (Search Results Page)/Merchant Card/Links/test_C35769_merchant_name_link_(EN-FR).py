import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def merchant_name():
    """
    >> This function verifies if the merchant name link is clickable and functional.
    """
    # Locating the merchant name link
    merchant_name = My.search_clickable_webelement(driver, By.TAG_NAME, "h3")
    assert merchant_name
    merchant_name.click()


def test_merchant_name():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    merchant_name()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    merchant_name()
    driver.quit()
