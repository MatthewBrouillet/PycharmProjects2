import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class CanPagesQuickLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def quick_links(self):
        """
        >> This function verifies if the Quick Links toogle is clickable and functional.
        """
        # Locating the Quick Links toggle
        quick_links_toggle = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="footer"]/div[1]/div[1]/a[1]')
        if quick_links_toggle:
            quick_links_toggle.click()
            pass
        else:
            return

        # Locating the Links container
        links_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]')
        if links_container:
            CanPagesQuickLinks.is_success = True
            return
        else:
            return

    def testing_quick_links(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.quick_links()
        if CanPagesQuickLinks.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesQuickLinks(driver)
test.testing_quick_links(My.canpages_web_link)
