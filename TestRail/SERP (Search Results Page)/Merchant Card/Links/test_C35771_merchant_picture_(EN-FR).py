import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def merchant_picture():
    """
    >> This function verifies if the merchant picture link is clickable and functional.
    """
    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Locating the merchant name link
    merchant_pic = My.search_clickable_webelement(driver, By.TAG_NAME, "img")
    assert merchant_pic
    merchant_pic.click()


def testing_merchant_picture():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    merchant_picture()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    merchant_picture()
    driver.quit()
