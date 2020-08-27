import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def business_discover_more():
    """
    >> This function verifies if the "Discover More" button is clickable
    >> and leads to "https://business.yellowpages.ca/home/#/"
    """
    # Locating the Discover More container
    container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[1]")
    assert container

    # Locating the Discover More button
    discover_more_button = My.search_clickable_webelement(container, By.XPATH,
                                                          "//*[@id='ypgFooter']/div[1]/div[1]/a/div")
    assert discover_more_button
    discover_more_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert "https://business.yellowpages.ca/home/#/" in url


def testing_business_discover_more():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    business_discover_more()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    business_discover_more()
    driver.quit()
