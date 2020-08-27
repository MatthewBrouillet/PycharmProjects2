import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def tips_ideas_grocery_view_more(link):
    """
    >> This function verifies if the "View more" link of "Grocery" in the Tips & Ideas' section is clickable
    >> and leads to "https://www.yellowpages.ca/tips/cat/food-beverage/grocery-tips/" or
    >> "https://www.pagesjaunes.ca/trucs/cat/aliments-boissons/epicerie/"
    """
    # Locating the Tips and Ideas container
    tips_ideas_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]")
    assert tips_ideas_container

    # Locating cards grid grocery container
    cards_grid_grocery = My.search_presence_webelement(
        tips_ideas_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[2]/div")
    assert cards_grid_grocery

    # Locating the View More link
    view_more_link = My.search_clickable_webelement(
        cards_grid_grocery, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[3]/div/div[3]/a")
    assert view_more_link
    view_more_link.click()

    # Validating the URL of the current web page
    url = driver.current_url
    if link == My.Testing_Env_EN:
        assert link + "/tips/cat/food-beverage/grocery-tips/" in url
    else:
        assert link + "/trucs/cat/aliments-boissons/epicerie/" in url


def test_tips_ideas_grocery_view_more():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    tips_ideas_grocery_view_more(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    tips_ideas_grocery_view_more(link)
    driver.quit()
