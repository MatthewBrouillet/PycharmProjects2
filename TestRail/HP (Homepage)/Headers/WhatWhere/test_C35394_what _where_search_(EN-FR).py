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
    assert link + '/search/si/1/restaurants/Montreal+QC' in url


def testing_what_where_search():
    """
    >> This function executes the steps of the test case
    """
    link = My.qa_web_link
    My.search_merchant_param(driver, link, 'restaurants', 'montreal')
    what_where_search(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_param(driver, link, 'restaurants', 'montreal')
    what_where_search(link)
    driver.quit()
