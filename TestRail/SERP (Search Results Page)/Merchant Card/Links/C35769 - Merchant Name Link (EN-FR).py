import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMerchantCardLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def merchant_name(self):
        """
        >> This function verifies if the merchant name link is clickable and functional.
        """
        # Locating the merchant name link
        merchant_name = My.search_clickable_webelement(driver, By.TAG_NAME, "h3")
        if merchant_name:
            merchant_name.click()
            YPMerchantCardLinks.is_success = True
            return
        else:
            return

    def testing_merchant_name(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.merchant_name()
        if YPMerchantCardLinks.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPMerchantCardLinks(driver)
test.testing_merchant_name(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_merchant_name(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
