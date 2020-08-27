import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def next_previous():
    """
    >> This function verifies if the next and previous buttons are clickable and functional.
    """
    # Locating the next button
    next_button = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[9]/div[2]/a")
    assert next_button
    next_button.click()

    # Locating the previous button
    previous_button = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[9]/div[2]/a[1]")
    assert previous_button
    previous_button.click()


def testing_next_previous():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    next_previous()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    next_previous()
    driver.quit()
