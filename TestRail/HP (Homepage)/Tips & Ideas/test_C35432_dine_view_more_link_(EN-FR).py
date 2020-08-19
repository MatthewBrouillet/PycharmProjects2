import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def tips_ideas_dine_view_more(link):
    """
    >> This function verifies if the "View more" link of "Dine" in the Tips & Ideas' section is clickable
    >> and leads to "https://www.yellowpages.ca/dine/" or "https://www.pagesjaunes.ca/resto/"
    """
    # Locating the Tips and Ideas container
    tips_ideas_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]")
    assert tips_ideas_container

    # Locating cards grid dine container
    cards_grid_dine = My.search_presence_webelement(
        tips_ideas_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[1]/div")
    assert cards_grid_dine

    # Locating the View More link
    view_more_link = My.search_clickable_webelement(
        cards_grid_dine, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[2]/div/div[3]/a")
    assert view_more_link
    view_more_link.click()

    # Validating the URL of the current web page
    if link == My.qa_web_link:
        url = driver.current_url[0:38]
        assert link + "/dine/" in url
    else:
        url = driver.current_url[0:43]
        assert link + "/resto/" in url


def test_tips_ideas_dine_view_more():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    tips_ideas_dine_view_more(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    tips_ideas_dine_view_more(link)
    driver.quit()
