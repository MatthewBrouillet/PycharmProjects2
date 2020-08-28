import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def pop_name_directory(link):
    """
    >> This function verifies that the Popular name directory toggle is clickable and functional.
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

    # Locating the Popular name directory link
    pop_name_directory = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[7]/a')
    assert pop_name_directory
    pop_name_directory.click()

    # Validating the URL of the current web page
    print(str(driver.current_url))
    url = driver.current_url
    assert link + 'popularnames/' in url


def testing_pop_name_directory():
    link = My.Testing_Env_c411_EN
    My.search_merchant_page(driver, link)
    pop_name_directory(link)
    driver.quit()
