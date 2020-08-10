import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class CanPagesWhatWhereSearch:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def what_where_search(self, link):
        """
        >> This function verifies if our search redirects you to /search/si/1/restaurants/Montreal+QC
        """
        # Validating the URL of the current web page
        print(str(driver.current_url))
        if driver.current_url == link + 'list.jsp?ct=M5H+3B7&na=restaurants':
            CanPagesWhatWhereSearch.is_success = True
            return
        else:
            return

    def testing_what_where_search(self, link, what, where):
        """
        >> This function executes the steps of the test case
        """
        My.search_canpages_param(driver, link, what, where)
        test.what_where_search(link)
        if CanPagesWhatWhereSearch.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = CanPagesWhatWhereSearch(driver)
test.testing_what_where_search(My.canpages_web_link, 'restaurants', '')
print('----------')
test.testing_what_where_search(My.canpages_fr_web_link, 'restaurants', '')
driver.quit()
sys.exit()
