import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def validate_ad_with_us(link):
    """
    >> This function verifies if clicking on "Advertise with us" redirects you to
    >> YellowPages for Business
    """
    # Locating the button on the top navigation bar
    button_ad_with_us = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[2]")
    assert button_ad_with_us
    button_ad_with_us.click()

    # Switching to the new window
    if link == My.Testing_Env_EN:
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
    else:
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)

    # Validates the URL of the current web page
    url = driver.current_url
    assert 'https://business.yellowpages.ca/home/#/' in url


def test_ad_with_us():
    """
    >> This function executes the steps of the test case
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    validate_ad_with_us(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    validate_ad_with_us(link)
    driver.quit()
