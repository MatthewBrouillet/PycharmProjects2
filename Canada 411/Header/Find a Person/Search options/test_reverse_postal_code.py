import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def reverse_postal_code_link(link):
    """
    >> This function verifies that the Reverse postal code toggle is clickable and functional.
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

    # Locating the Reverse postal code link
    rev_postal_code = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[4]/a')
    assert rev_postal_code
    rev_postal_code.click()

    # Validating the URL of the current web page
    print(str(driver.current_url))
    url = driver.current_url
    assert link + 'postal-code-lookup/' in url


def testing_reverse_postal_code_link():
    link = My.c411_qa_web_link
    My.search_merchant_page(driver, link)
    reverse_postal_code_link(link)
    driver.quit()
