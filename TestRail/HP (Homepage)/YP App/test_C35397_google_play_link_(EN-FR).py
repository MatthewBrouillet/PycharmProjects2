import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def yp_app_google_play_link():
    """
    >> This function verifies if the "Google Play" link is clickable
    >> and leads to "/applications/?pid=YPmobile_home"
    """
    # Locating the YP App container
    yp_app_links_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[1]/div[2]")
    assert yp_app_links_container

    # Locating the Google Play button
    google_play_button = My.search_clickable_webelement(yp_app_links_container, By.XPATH,
                                                        "//*[@id='ypgFooter']/div[1]/div[2]/a[1]/div/div")
    assert google_play_button
    google_play_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert My.yp_web_link + "/applications/?pid=YPmobile_home" in url


def test_yp_app_google_play_link():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.qa_web_link)
    yp_app_google_play_link()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link)
    yp_app_google_play_link()
    driver.quit()
