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

    def merchant_logo_tool_tip(self):
        """
        >> This function verifies if the merchant logo tool tip is present.
        """
        # Locating the first merchant card
        first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
        if first_merchant_card:
            pass
        else:
            return

        # Validating the presence of the tool tip
        merchant_logo = My.search_presence_webelement(first_merchant_card, By.TAG_NAME, "img")
        if merchant_logo:
            if merchant_logo.get_attribute("alt") is not None:
                print(str(merchant_logo.get_attribute("alt")))
                YPMerchantCardLinks.is_success = True
                return
            else:
                return
        else:
            return

    def testing_merchant_logo_tool_tip(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.merchant_logo_tool_tip()
        if YPMerchantCardLinks.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPMerchantCardLinks(driver)
test.testing_merchant_logo_tool_tip(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_merchant_logo_tool_tip(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
