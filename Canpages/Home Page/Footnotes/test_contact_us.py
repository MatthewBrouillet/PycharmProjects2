import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def contact_us():
    """
    >> This function verifies if the Contact Us toggle is clickable and functional.
    """
    # Locating the Contact Us toggle
    contact_us_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[2]")
    assert contact_us_toggle
    contact_us_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert My.yp_web_link + "/contactus" in url


def testing_contact_us():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.canpages_web_link)
    contact_us()
    driver.quit()
