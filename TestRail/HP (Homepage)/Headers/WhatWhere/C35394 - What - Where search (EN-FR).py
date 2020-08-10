import sys
import myModule as My
from selenium import webdriver

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWhatWhereSearch:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def what_where_search(self, link):
        """
        >> This function verifies if our search redirects you to /search/si/1/restaurants/Montreal+QC
        """
        # Validating the URL of the current web page
        if driver.current_url == link + '/search/si/1/restaurants/Montreal+QC':
            YPWhatWhereSearch.is_success = True
            return
        else:
            return

    def testing_what_where_search(self, link, what, where):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_param(driver, link, what, where)
        test.what_where_search(link)
        if YPWhatWhereSearch.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPWhatWhereSearch(driver)
test.testing_what_where_search(My.yp_web_link, 'restaurants', 'montreal')
print('----------')
test.testing_what_where_search(My.pj_web_link, 'restaurants', 'montreal')
driver.quit()
sys.exit()
