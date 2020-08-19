import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def tips_ideas_home_service_view_more(link):
    """
    >> This function verifies if the "View more" link of "Home Services" in the Tips & Ideas' section is clickable
    >> and leads to "https://www.yellowpages.ca/home-services" or "https://www.pagesjaunes.ca/services-pro"
    """
    # Locating the Tips and Ideas container
    tips_ideas_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]")
    assert tips_ideas_container

    # Locating cards grid home services container
    cards_grid_home_services = My.search_presence_webelement(
        tips_ideas_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[1]/div")
    assert cards_grid_home_services

    # Locating the View More link
    view_more_link = My.search_clickable_webelement(
        cards_grid_home_services, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[1]/div/div[3]/a")
    assert view_more_link
    view_more_link.click()

    # Validating the URL of the current web page
    url = driver.current_url
    if link == My.qa_web_link:
        assert link + "/home-services" in url
    else:
        assert link + "/services-pro" in url


def testing_tips_ideas_home_service_view_more():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    tips_ideas_home_service_view_more(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    tips_ideas_home_service_view_more(link)
    driver.quit()
