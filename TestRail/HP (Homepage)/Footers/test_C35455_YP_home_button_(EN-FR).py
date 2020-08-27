import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def yp_home(link):
    """
    >> This function verifies if the PJ Home logo in the footer section is clickable
    >> and leads to yp.ca or pj.ca home page
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[2]")
    assert footer_container

    # Locating the YP home button
    yp_home_button = My.search_clickable_webelement(
        footer_container, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[1]/div[1]/a/span")
    assert yp_home_button
    yp_home_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert link + "/" in url


def test_yp_home():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    yp_home(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    yp_home(link)
    driver.quit()
