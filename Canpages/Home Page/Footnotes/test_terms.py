import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def terms():
    """
    >> This function verifies if the Terms toggle is clickable and functional.
    """
    # Locating the Terms toggle
    terms_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[5]")
    assert terms_toggle
    terms_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert My.corporate_web_link + 'legal-notice/terms-of-use-agreement/' in url


def testing_terms():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.canpages_web_link)
    terms()
    driver.quit()
