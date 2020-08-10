import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPNbrSearchResults:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def nbr_search_results(self, link):
        """
        >> This function verifies if the number of search results is displayed.
        """
        # Locating the result number display
        nbr_search_results = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[1]/h1/span")
        if nbr_search_results is not None:
            print(nbr_search_results.text)
            YPNbrSearchResults.is_success = True
            return
        else:
            return

    def testing_nbr_search_results(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.nbr_search_results(link)
        if YPNbrSearchResults.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPNbrSearchResults(driver)
test.testing_nbr_search_results(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_nbr_search_results(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
