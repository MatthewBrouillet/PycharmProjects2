import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def validate_people_search(link):
    """
    >> This function verifies if clicking on "People search" redirects you to
    >> canada411.ca
    """
    # Locating the button on the top navigation bar
    button_people_search = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[1]")
    assert button_people_search
    button_people_search.click()

    # Validating the URL of the current web page
    url = driver.current_url
    if link == My.Testing_Env_EN:
        assert 'https://www.canada411.ca/' in url
    else:
        assert 'https://www.fr.canada411.ca/' in url


def testing_people_search():
        """
        >> This function executes the steps of the test case
        """
        link = My.Testing_Env_EN
        My.search_merchant_page(driver, link)
        validate_people_search(link)
        print('----------')
        link = My.Testing_Env_FR
        My.search_merchant_page(driver, link)
        validate_people_search(link)
        driver.quit()
