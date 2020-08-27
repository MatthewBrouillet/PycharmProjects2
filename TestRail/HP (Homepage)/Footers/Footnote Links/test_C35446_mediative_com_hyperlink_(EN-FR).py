import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def mediative_toggle(link):
    """
    >> This function verifies if the Categories drop down menu is clickable and functional
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p')
    assert footer_container

    # Locating the mediative.com link
    mediative_hyperlink = My.search_clickable_webelement(
        footer_container, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p/span[1]/a[1]')
    assert mediative_hyperlink
    mediative_hyperlink.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link in url


def test_mediative_toggle():
    """
    >> This function executes the steps of the test case
    """
    link = My.yp_web_link
    My.search_merchant_page(driver, My.Testing_Env_EN)
    mediative_toggle(link)
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    mediative_toggle(link)
    driver.quit()
