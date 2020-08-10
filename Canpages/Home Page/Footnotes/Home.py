import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class CanPagesFootnotes:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def home(self, link):
        """
        >> This function verifies if the Home toggle is clickable and functional.
        """
        # Locating the Home toggle
        home_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[1]")
        if home_toggle:
            home_toggle.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link:
            CanPagesFootnotes.is_success = True
            return
        else:
            return

    def testing_home(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.home(link)
        if CanPagesFootnotes.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesFootnotes(driver)
test.testing_home(My.canpages_web_link)
