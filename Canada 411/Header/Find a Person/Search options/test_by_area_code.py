import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def by_area_code_link(link):
    """
    >> This function verifies that the By area code toggle is clickable and functional.
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

    # Locating the By area code link
    by_area_code = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[6]/a')
    assert by_area_code
    by_area_code.click()

    # Validating the URL of the current web page
    print(str(driver.current_url))
    url = driver.current_url
    assert link + 'area-code-lookup/' in url


def testing_by_area_code_link():
    link = My.Testing_Env_c411_EN
    My.search_merchant_page(driver, link)
    by_area_code_link(link)
    driver.quit()
