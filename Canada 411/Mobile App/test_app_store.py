import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def app_store():
    """
    >> This function verifies that the App Store button is clickable and functional.
    """
    # Locating the Mobile App container
    mobile_app_container = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]')
    assert mobile_app_container

    # Locating the App Store button
    app_store_button = My.search_clickable_webelement(
        mobile_app_container, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]/div/div[2]/ul/li[1]/a')
    assert app_store_button
    app_store_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert 'https://apps.apple.com/CA/app/id322964940?mt=8' in url


def test_app_store():
    My.search_merchant_page(driver, My.Testing_Env_c411_EN)
    app_store()
    driver.quit()
