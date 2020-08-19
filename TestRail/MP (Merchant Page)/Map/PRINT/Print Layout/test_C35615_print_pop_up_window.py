import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def print_popup():
    """
    >> This function verifies if the print option is present and clickable.
    """
    current_location_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='DRIVING']/form/div[2]/div[1]/span[3]")
    assert current_location_button
    current_location_button.click()

    print_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='DRIVING']/div/div[5]/button")
    assert print_button
    print_button.click()


def test_print_popup():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/merchant/directions/1329952")
    print_popup()
    driver.quit()
