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

    def opening_hours(self):
        """
        >> This function verifies if the merchant name link is clickable and functional.
        """
        # Locating the first merchant card
        first_merchant_card = My.search_presence_webelement(
            driver, By.CLASS_NAME, "listing__content__wrapper")
        if first_merchant_card:
            pass
        else:
            return

        # Locating the merchant name link
        opening_hours_link = My.search_clickable_webelement(
            first_merchant_card, By.XPATH, "//div//div//div//div//div//a")
        if opening_hours_link:
            opening_hours_link.click()
            YPMerchantCardLinks.is_success = True
            return
        else:
            return

    def testing_opening_hours(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.opening_hours()
        if YPMerchantCardLinks.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPMerchantCardLinks(driver)
test.testing_opening_hours(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_opening_hours(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
