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

    def business_directory(self, link):
        """
        >> This function verifies if the Business Directory toggle is clickable and functional.
        """
        # Locating the Contact Us toggle
        business_directory_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[6]")
        if business_directory_toggle:
            business_directory_toggle.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link + 'directory':
            CanPagesFootnotes.is_success = True
            return
        else:
            return

    def testing_business_directory(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.business_directory(link)
        if CanPagesFootnotes.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesFootnotes(driver)
test.testing_business_directory(My.canpages_web_link)
