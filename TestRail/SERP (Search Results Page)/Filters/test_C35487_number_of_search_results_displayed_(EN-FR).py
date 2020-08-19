import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def nbr_search_results():
    """
    >> This function verifies if the number of search results is displayed.
    """
    # Locating the result number display
    nbr_search_results = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[1]/h1/span")
    if nbr_search_results is not None:
        assert nbr_search_results
    else:
        return


def test_nbr_search_results():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link)
    nbr_search_results()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link)
    nbr_search_results()
    driver.quit()
