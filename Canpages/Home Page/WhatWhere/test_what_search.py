import myModule as My
from selenium import webdriver

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def what_where_search(link):
    """
    >> This function verifies if our search redirects you to /search/si/1/restaurants/Montreal+QC
    """
    # Validating the URL of the current web page
    url = driver.current_url
    print(str(driver.current_url))
    assert link + 'list.jsp?ct=M5H+3B7&na=restaurants' in url


def testing_what_where_search():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_canpages_param(driver, My.canpages_web_link, 'restaurants', '')
    what_where_search(link)
    driver.quit()
