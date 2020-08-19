import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def ypca_toggle(link):
    """
    >> This function verifies if the YPCA hyperlink redirects you to yp.ca home page
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p')
    assert footer_container

    # Locating the YP.ca link
    ypca_hyperlink = My.search_clickable_webelement(
        footer_container, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p/span[1]/a[2]')
    assert ypca_hyperlink
    ypca_hyperlink.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link in url


def test_ypca_toggle():
    """
    >> This function executes the steps of the test case
    """
    link = My.yp_web_link
    My.search_merchant_page(driver, My.qa_web_link)
    ypca_toggle(link)
    print('----------')
    link = My.pj_web_link
    My.search_merchant_page(driver, My.qa_fr_web_link)
    ypca_toggle(link)
    driver.quit()
