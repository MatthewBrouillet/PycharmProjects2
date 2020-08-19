import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def by_address_link():
    """
    >> This function verifies that the By address toggle is clickable and functional.
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

    # Locating the By address link
    by_address = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/ul/li[3]/a')
    assert by_address
    by_address.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert 'https://canada411.yellowpages.ca/search/address.html' in url


def test_by_address_link():
    My.search_merchant_page(driver, My.c411_qa_web_link)
    by_address_link()
    driver.quit()
