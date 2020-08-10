import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMerchantPageMap:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def mini_map(self):
        """
        >> This function verifies if clicking View Map on the mini map redirects you to the direction page.
        """
        first_merchant_card = My.search_presence_webelement(
            driver, By.CLASS_NAME, "listing__content__wrapper")
        if first_merchant_card:
            pass
        else:
            return

        merchant_name = My.search_clickable_webelement(
            first_merchant_card, By.TAG_NAME, "h3")
        if merchant_name:
            merchant_name.click()
            pass
        else:
            return

        mini_map = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="ypgBody"]/div[3]/div/div[4]/div[2]/div[2]/div[2]/div[2]/ul/li/a')
        if mini_map:
            mini_map.click()
            pass
        else:
            return

        if driver.current_url[26:47] == '/merchant/directions/':
            YPMerchantPageMap.is_success = True
            return
        else:
            return

    def testing_mini_map(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.mini_map()
        if YPMerchantPageMap.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPMerchantPageMap(driver)
test.testing_mini_map(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_mini_map(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
