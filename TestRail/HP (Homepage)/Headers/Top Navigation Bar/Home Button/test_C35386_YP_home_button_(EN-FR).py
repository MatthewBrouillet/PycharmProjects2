import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def home_yp_button(link):
    """
    >> This function verifies if the home YP / PJ button leads to yp.ca / pj.ca
    """
    # Locating the home button on the top navigation bar
    home_yp_button = My.search_clickable_webelement(driver, By.ID, "QAypLogoLhs")
    assert home_yp_button
    home_yp_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link in url


def test_home_yp_button():
    """
    >> This function executes the steps of the test case
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    home_yp_button(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    home_yp_button(link)
    driver.quit()
