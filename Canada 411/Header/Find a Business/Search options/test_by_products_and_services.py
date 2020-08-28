import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def by_products_services_link():
    """
    >> This function verifies that the By products & services is clickable and functional.
    """
    # Locating the Find a Business container
    find_a_business_container = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]')
    assert find_a_business_container

    # Locating the More search options toggle
    more_search_options_toggle = My.search_clickable_webelement(
        find_a_business_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/a')
    assert more_search_options_toggle
    more_search_options_toggle.click()

    # Locating the By products & services link
    by_products_services = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/ul/li[6]/a')
    assert by_products_services
    by_products_services.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert 'https://canada411.yellowpages.ca/products/' in url


def test_by_products_services_link():
    My.search_merchant_page(driver, My.Testing_Env_c411_EN)
    by_products_services_link()
    driver.quit()
