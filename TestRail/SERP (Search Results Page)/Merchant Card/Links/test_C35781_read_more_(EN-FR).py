import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def read_more():
    """
    >> This function verifies if the merchant name link is clickable and functional.
    """
    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Locating the merchant name link
    read_more_link = My.search_clickable_webelement(first_merchant_card, By.XPATH, "//span[2]//a")
    assert read_more_link
    read_more_link.click()


def test_read_more():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    read_more()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    read_more()
    driver.quit()
