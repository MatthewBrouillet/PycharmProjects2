import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def connect_with_facebook():
    """
    >> This function verifies that the Connect with Facebook button is clickable and functional.
    """
    # Locating the Social container
    social_container = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[2]')
    assert social_container

    # Locating the Connect with Facebook button
    connect_with_facebook_button = My.search_clickable_webelement(
        social_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/a')
    assert connect_with_facebook
    connect_with_facebook_button.click()


def test_connect_with_facebook():
    My.search_merchant_page(driver, My.Testing_Env_c411_EN)
    connect_with_facebook()
    driver.quit()
