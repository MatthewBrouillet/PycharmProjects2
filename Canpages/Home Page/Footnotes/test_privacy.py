import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def privacy():
    """
    >> This function verifies if the Privacy toggle is clickable and functional.
    """
    # Locating the Privacy toggle
    privacy_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[4]")
    assert privacy_toggle
    privacy_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert My.corporate_web_link + 'legal-notice/privacy-statement/' in url


def testing_privacy():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.canpages_web_link)
    privacy()
    driver.quit()
