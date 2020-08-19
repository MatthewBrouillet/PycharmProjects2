import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def home(link):
    """
    >> This function verifies if the Home toggle is clickable and functional.
    """
    # Locating the Home toggle
    home_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[1]")
    assert home_toggle
    home_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link in url


def testing_home():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    home(link)
    driver.quit()
