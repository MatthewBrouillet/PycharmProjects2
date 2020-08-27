import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def more():
    """
    >> This function verifies if the merchant name link is clickable and functional.
    """
    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Locating the merchant name link
    more_link = My.search_clickable_webelement(first_merchant_card, By.XPATH, "//article//a")
    assert more_link
    more_link.click()


def test_more():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    more()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    more()
    driver.quit()
