import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def more_search_options_toggle():
    """
    >> This function verifies that the More search options toggle is clickable and functional.
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

    # Locating the drop down menu
    drop_down_menu = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul')
    assert drop_down_menu


def testing_more_search_options_toggle():
    My.search_merchant_page(driver, My.c411_qa_web_link)
    more_search_options_toggle()
    driver.quit()
