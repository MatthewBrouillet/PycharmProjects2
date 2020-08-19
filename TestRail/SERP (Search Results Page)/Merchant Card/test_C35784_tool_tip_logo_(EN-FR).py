import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def merchant_logo_tool_tip():
    """
    >> This function verifies if the merchant logo tool tip is present.
    """
    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Validating the presence of the tool tip
    merchant_logo = My.search_presence_webelement(first_merchant_card, By.TAG_NAME, "img")
    assert merchant_logo

    assert merchant_logo.get_attribute("alt") is not None
    print(str(merchant_logo.get_attribute("alt")))


def test_merchant_logo_tool_tip():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    merchant_logo_tool_tip()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    merchant_logo_tool_tip()
    driver.quit()
