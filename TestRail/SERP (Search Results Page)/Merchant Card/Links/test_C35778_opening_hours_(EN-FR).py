import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def opening_hours():
    """
    >> This function verifies if the merchant name link is clickable and functional.
    """
    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Locating the merchant name link
    opening_hours_link = My.search_clickable_webelement(first_merchant_card, By.XPATH, "//div//div//div//div//div//a")
    assert opening_hours_link
    opening_hours_link.click()


def testing_opening_hours():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    opening_hours()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    opening_hours()
    driver.quit()
