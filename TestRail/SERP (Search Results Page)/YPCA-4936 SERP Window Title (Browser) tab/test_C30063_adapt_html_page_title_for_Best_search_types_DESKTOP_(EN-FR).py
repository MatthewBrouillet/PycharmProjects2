import myModule as My
from selenium import webdriver

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def window_title(link):
    """
    >> This function verifies the window title for the "best" search results
    """
    # Locating the displayed text
    if link == My.Testing_Env_EN + "/search/si/1/restaurants/Montreal+QC":
        assert driver.title == "The Best restaurants in Montreal | YellowPages.ca™"
    else:
        assert driver.title == "Les meilleur(e)s restaurants à Montréal | PagesJaunes.ca(MC)"


def test_window_title():
    """
    >> This function executes the steps of the test case
    """
    link = My.Testing_Env_EN + "/search/si/1/restaurants/Montreal+QC"
    My.search_merchant_page(driver, link)
    window_title(link)
    print('----------')
    link = My.Testing_Env_FR + "/search/si/1/restaurants/Montreal+QC"
    My.search_merchant_page(driver, link)
    window_title(link)
    driver.quit()
