import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def validate(link):
    """
    >> This function verifies if, when you click on the EN / FR button,
    >> the page is redirected to yellowpages.ca / pagesjaunes.ca
    """
    # Locating the language toggle
    lang_toggle = My.search_clickable_webelement(driver, By.ID, "lang-switch")
    assert lang_toggle
    lang_toggle.click()

    # Validating the URL of the current web page
    url = driver.current_url
    if link == My.canpages_web_link:
        assert My.canpages_fr_web_link in url

    else:
        assert My.canpages_web_link in url


def testing_validate():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    validate(link)
    print('----------')
    link = My.canpages_fr_web_link
    My.search_merchant_page(driver, link)
    validate(link)
    driver.quit()
