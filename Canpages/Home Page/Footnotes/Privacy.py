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

    def privacy(self):
        """
        >> This function verifies if the Privacy toggle is clickable and functional.
        """
        # Locating the Privacy toggle
        privacy_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[4]")
        if privacy_toggle:
            privacy_toggle.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == My.corporate_web_link + 'legal-notice/privacy-statement/':
            CanPagesFootnotes.is_success = True
            return
        else:
            return

    def testing_privacy(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.privacy()
        if CanPagesFootnotes.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesFootnotes(driver)
test.testing_privacy(My.canpages_web_link)
