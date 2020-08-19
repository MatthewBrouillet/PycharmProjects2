import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def corporate():
    """
    >> This function verifies if the Corporate toggle is clickable and functional.
    """
    # Locating the Corporate toggle
    corporate_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[3]")
    assert corporate_toggle
    corporate_toggle.click()

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    # Validating the URL of the current web page
    url = driver.current_url
    assert My.corporate_web_link in url


def testing_corporate():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.canpages_web_link)
    corporate()
    driver.quit()
