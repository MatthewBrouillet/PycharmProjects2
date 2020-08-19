import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def opening_hours():
    """
    >> This function verifies if the opening hours of the merchant are displayed on the merchant card.
    """
    # Locating the Opening hours of the merchant
    hours = My.search_presence_webelement(
        driver, By.XPATH,
        '//*[@id="ypgBody"]/div[2]/div/div[1]/div[9]/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/a')
    assert hours
    print(str(hours.text))


def testing_opening_hours():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    opening_hours()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    opening_hours()
    driver.quit()
