import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def print_option_driving():
    """
    >> This function verifies if the print option is present and clickable.
    """
    # Locating the current location button
    current_location_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='DRIVING']/form/div[2]/div[1]/span[3]")
    assert current_location_button
    current_location_button.click()

    # Locating the print button
    print_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='DRIVING']/div/div[5]/button")
    assert print_button

    # Locating the FR language toggle
    fr_toggle = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[2]/a")
    assert fr_toggle
    fr_toggle.click()

    # Locating the current location button
    current_location_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='DRIVING']/form/div[2]/div[1]/span[3]")
    assert current_location_button
    current_location_button.click()

    # Locating the print button
    print_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='DRIVING']/div/div[5]/button")
    assert print_button


def test_print_option_driving():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/merchant/directions/1329952")
    print_option_driving()
    driver.quit()
