import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPyphyperlink:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def ypca_toggle(self, link):
        """
        >> This function verifies if the YPCA hyperlink redirects you to yp.ca home page
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p')
        if footer_container:
            pass
        else:
            return

        # Locating the YP.ca link
        ypca_hyperlink = My.search_clickable_webelement(
            footer_container, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p/span[1]/a[2]')
        if ypca_hyperlink:
            ypca_hyperlink.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link + '/':
            YPyphyperlink.is_success = True
            return
        else:
            return

    def testing_ypca_toggle(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.ypca_toggle(link)
        if YPyphyperlink.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPyphyperlink(driver)
test.testing_ypca_toggle(My.yp_web_link)
print('----------')
test.testing_ypca_toggle(My.pj_web_link)
driver.quit()
sys.exit()
