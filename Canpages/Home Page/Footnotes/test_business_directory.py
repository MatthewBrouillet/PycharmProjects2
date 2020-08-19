import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def business_directory(link):
    """
    >> This function verifies if the Business Directory toggle is clickable and functional.
    """
    # Locating the Contact Us toggle
    business_directory_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[6]")
    assert business_directory_toggle
    business_directory_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link + 'directory' in url


def testing_business_directory():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    business_directory(link)
    driver.quit()
