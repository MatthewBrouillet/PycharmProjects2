import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def home_canpages_button(link):
    """
    >> This function verifies if the home YP / PJ button leads to yp.ca / pj.ca
    """
    # Locating the home button on the top navigation bar
    home_canpages_button = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='search-bar-top']/span/a/img")
    assert home_canpages_button
    home_canpages_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link in url


def testing_home_canpages_button():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    home_canpages_button(link)
    print('----------')
    link = My.canpages_fr_web_link
    My.search_merchant_page(driver, link)
    home_canpages_button(link)
    driver.quit()
