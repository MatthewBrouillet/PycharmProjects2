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

    def corporate(self):
        """
        >> This function verifies if the Corporate toggle is clickable and functional.
        """
        # Locating the Corporate toggle
        corporate_toggle = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='footer-nav']/a[3]")
        if corporate_toggle:
            corporate_toggle.click()
            pass
        else:
            return

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        # Validating the URL of the current web page
        if driver.current_url == My.corporate_web_link:
            CanPagesFootnotes.is_success = True
            return
        else:
            return

    def testing_corporate(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.corporate()
        if CanPagesFootnotes.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesFootnotes(driver)
test.testing_corporate(My.canpages_web_link)
