import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def estimated_travel_time():
    """
    >> This function verifies if the estimated travel time of the merchant are displayed when the button is clicked.
    """
    estimated_travel_time_button = My.search_clickable_webelement(
        driver, By.CSS_SELECTOR, '#ypgBody > div.page__container > div > '
                          'div.page__container.page__container--full.page__container--merchant '
                          '> div.page__content > div:nth-child(2) > div.merchant__travel-time > button')
    assert estimated_travel_time_button
    estimated_travel_time_button.click()


def testing_estimated_travel_time():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918.html")
    estimated_travel_time()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918.html")
    estimated_travel_time()
    driver.quit()
