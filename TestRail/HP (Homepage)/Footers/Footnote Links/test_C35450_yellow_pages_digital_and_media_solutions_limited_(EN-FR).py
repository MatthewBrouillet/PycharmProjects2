import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def media_solutions_toggle(link):
    """
    >> This function verifies if the YP Digital & Media Solutions hyperlink
    >> redirects you to yp corporate home page.
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p')
    assert footer_container

    # Locating the media solutions link
    media_solutions_hyperlink = My.search_clickable_webelement(
        footer_container, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p/span[1]/a[3]')
    assert media_solutions_hyperlink
    media_solutions_hyperlink.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link in url


def test_media_solutions_toggle():
    """
    >> This function executes the steps of the test case
    """
    link = My.corporate_web_link
    My.search_merchant_page(driver, My.Testing_Env_EN)
    media_solutions_toggle(link)
    print('----------')
    link = My.entreprise_web_link
    My.search_merchant_page(driver, My.Testing_Env_FR)
    media_solutions_toggle(link)
    driver.quit()
