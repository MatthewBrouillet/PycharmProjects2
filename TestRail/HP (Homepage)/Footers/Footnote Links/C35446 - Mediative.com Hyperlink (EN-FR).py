import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMediative:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def mediative_toggle(self, link):
        """
        >> This function verifies if the Categories drop down menu is clickable and functional
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p')
        if footer_container:
            pass
        else:
            return

        # Locating the mediative.com link
        mediative_hyperlink = My.search_clickable_webelement(
            footer_container, By.XPATH, '//*[@id="ypgFooter"]/div[2]/p/span[1]/a[1]')
        if mediative_hyperlink:
            mediative_hyperlink.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link + '/':
            YPMediative.is_success = True
            return
        else:
            return

    def testing_mediative_toggle(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.mediative_toggle(link)
        if YPMediative.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPMediative(driver)
test.testing_mediative_toggle(My.yp_web_link)
print('----------')
test.testing_mediative_toggle(My.pj_web_link)
driver.quit()
sys.exit()
