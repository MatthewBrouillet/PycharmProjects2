import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPSearch:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def validate_people_search(self, link):
        """
        >> This function verifies if clicking on "People search" redirects you to
        >> canada411.ca
        """
        # Locating the button on the top navigation bar
        button_people_search = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[1]")
        if button_people_search:
            button_people_search.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if link == My.yp_web_link:
            if driver.current_url == 'https://www.canada411.ca/':
                YPSearch.is_success = True
                return
            else:
                return
        else:
            if driver.current_url == 'https://www.fr.canada411.ca/':
                YPSearch.is_success = True
                return
            else:
                return

    def testing_people_search(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.validate_people_search(link)
        if YPSearch.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPSearch(driver)
test.testing_people_search(My.yp_web_link)
print('----------')
test.testing_people_search(My.pj_web_link)
driver.quit()
sys.exit()
