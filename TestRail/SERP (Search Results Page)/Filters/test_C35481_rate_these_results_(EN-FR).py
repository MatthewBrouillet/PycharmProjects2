import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def rate_these_results():
    """
    >> This function verifies if the Rate these results toggle is clickable and leads to a pop up window
    """
    # Locating the Rate these results toggle
    rate_these_results = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/a")
    assert rate_these_results
    rate_these_results.click()

    # Locating the Rate these results pop-up window
    rate_pop_up = My.search_presence_webelement(
        rate_these_results, By.XPATH, "//*[@id='ypModaRateResult']/div/div")
    assert rate_pop_up


def test_rate_these_results():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    rate_these_results()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    rate_these_results()
    driver.quit()
