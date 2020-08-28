import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def reverse_phone_link(link):
    """
    >> This function verifies that the Reverse phone toggle is clickable and functional.
    """
    # Locating the Find a Person container
    find_a_person_container = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]')
    assert find_a_person_container

    # Locating the More search options toggle
    more_search_options_toggle = My.search_clickable_webelement(
        find_a_person_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/a')
    assert more_search_options_toggle
    more_search_options_toggle.click()

    # Locating the Reverse phone link
    rev_phone = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[3]/a')
    assert rev_phone
    rev_phone.click()

    # Validating the URL of the current web page
    print(str(driver.current_url))
    url = driver.current_url
    assert link + 'search/reverse.html' in url


def testing_reverse_phone_link():
    link = My.Testing_Env_c411_EN
    My.search_merchant_page(driver, link)
    reverse_phone_link(link)
    driver.quit()
