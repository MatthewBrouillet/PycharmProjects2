import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def by_category_link():
    """
    >> This function verifies that the By category toggle is clickable and functional.
    """
    # Locating the Find a Business container
    find_a_business_container = My.search_presence_webelement(driver, By.XPATH,
                                                              '//*[@id="c411ContentArea"]/div[1]/div[2]')
    assert find_a_business_container

    # Locating the More search options toggle
    more_search_options_toggle = My.search_clickable_webelement(
        find_a_business_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/a')
    assert more_search_options_toggle
    more_search_options_toggle.click()

    # Locating the By category link
    by_category = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/ul/li[4]/a')
    assert by_category
    by_category.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert 'https://canada411.yellowpages.ca/business/' in url


def test_by_category_link():
    My.search_merchant_page(driver, My.c411_qa_web_link)
    by_category_link()
    driver.quit()
