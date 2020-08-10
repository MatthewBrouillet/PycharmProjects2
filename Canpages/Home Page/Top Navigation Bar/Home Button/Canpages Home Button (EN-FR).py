import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class CanPagesHomeButton:
    def __init__(self, driver):
        self.driver = driver

    # Class Variables
    is_success = False

    def home_canpages_button(self, link):
        """
        >> This function verifies if the home YP / PJ button leads to yp.ca / pj.ca
        """
        # Locating the home button on the top navigation bar
        home_canpages_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='search-bar-top']/span/a/img")
        if home_canpages_button:
            home_canpages_button.click()
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link:
            CanPagesHomeButton.is_success = True
            return
        else:
            return

    def testing_home_canpages_button(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.home_canpages_button(link)
        if CanPagesHomeButton.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = CanPagesHomeButton(driver)
test.testing_home_canpages_button(My.canpages_web_link)
print('----------')
test.testing_home_canpages_button(My.canpages_fr_web_link)
driver.quit()
sys.exit()
