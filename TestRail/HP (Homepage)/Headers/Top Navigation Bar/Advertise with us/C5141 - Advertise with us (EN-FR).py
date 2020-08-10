import sys
import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPAd:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def validate_ad_with_us(self):
        """
        >> This function verifies if clicking on "Advertise with us" redirects you to
        >> YellowPages for Business
        """
        # Locating the button on the top navigation bar
        button_ad_with_us = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[2]")
        if button_ad_with_us:
            button_ad_with_us.click()
            pass
        else:
            return

        # Switching to the new window
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        # Validates the URL of the current web page
        if driver.current_url == 'https://business.yellowpages.ca/home/#/':
            YPAd.is_success = True
            return
        else:
            return

    def testing_ad_with_us(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.validate_ad_with_us()
        if YPAd.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPAd(driver)
test.testing_ad_with_us(My.yp_web_link)
print('----------')
test.testing_ad_with_us(My.pj_web_link)
driver.quit()
sys.exit()
