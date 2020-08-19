import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def validate():
    """
    >> This function verifies if, when you click on the EN / FR button,
    >> the page is redirected to yellowpages.ca / pagesjaunes.ca
    """
    # Locating the language toggle
    lang_toggle = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[6]/a")
    assert lang_toggle
    lang_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url[0:33]
    assert 'https://qa-ui-mtl.pagesjaunes.ca/' in url

    # Locating the language toggle
    lang_toggle = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[6]/a")
    assert lang_toggle
    lang_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url[0:33]
    assert 'https://qa-ui-mtl.yellowpages.ca/' in url


def test_validate():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link)
    validate()
    driver.quit()
