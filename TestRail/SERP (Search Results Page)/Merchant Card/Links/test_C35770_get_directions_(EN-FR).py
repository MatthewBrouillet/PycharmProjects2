import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def get_directions():
    """
    >> This function verifies if the merchant name link is clickable and functional.
    """
    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Locating the merchant name link
    get_directions = My.search_clickable_webelement(
        first_merchant_card, By.XPATH, "//div//div//div//div//div//div//a")
    assert get_directions
    get_directions.click()


def test_get_directions():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    get_directions()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    get_directions()
    driver.quit()
