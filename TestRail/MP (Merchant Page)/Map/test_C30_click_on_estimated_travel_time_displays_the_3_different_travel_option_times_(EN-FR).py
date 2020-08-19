import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def estimated_travel_time():
    """
    >> This function verifies if the estimated travel time of the merchant are displayed when the button is clicked.
    """
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    merchant_name = My.search_clickable_webelement(first_merchant_card, By.TAG_NAME, "h3")
    assert merchant_name
    merchant_name.click()

    estimated_travel_time_button = My.search_clickable_webelement(
        driver, By.CSS_SELECTOR, '#ypgBody > div.page__container > div > '
                          'div.page__container.page__container--full.page__container--merchant '
                          '> div.page__content > div:nth-child(2) > div.merchant__travel-time > button')
    assert estimated_travel_time_button
    estimated_travel_time_button.click()

    count = 1
    while count < 4:
        travel_option_time = My.search_presence_webelement(
            driver, By.XPATH,
            '//*[@id="ypgBody"]/div[3]/div/div[4]/div[2]/div[2]/div[4]/div/div/div[' + str(count) + ']/a')

        if count == 1:
            assert travel_option_time

        elif count == 2:
            assert travel_option_time

        else:
            assert travel_option_time

        count += 1


def testing_estimated_travel_time():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    estimated_travel_time()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    estimated_travel_time()
    driver.quit()
