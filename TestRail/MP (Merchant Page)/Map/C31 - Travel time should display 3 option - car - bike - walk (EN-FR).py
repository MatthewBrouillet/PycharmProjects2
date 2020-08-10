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
    driving_is_success = False
    walking_is_success = False
    cycling_is_success = False

    def travel_options(self, link):
        """
        >> This function verifies if the 3 travel options are displayed on the merchant page.
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
            pass
        else:
            return

        current_location_icon = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="DRIVING"]/form/div[2]/div[1]/span[3]')
        if current_location_icon:
            current_location_icon.click()
            pass
        else:
            return

        count = 1
        while count < 4:
            travel_option = My.search_presence_webelement(
                driver, By.XPATH, '//*[@id="DRIVING"]/form/div[1]/ul/li[' + str(count) + ']/a')
            if count == 1:
                if travel_option:
                    YPMerchantPageMap.driving_is_success = True
                else:
                    pass
            elif count == 2:
                if travel_option:
                    YPMerchantPageMap.walking_is_success = True
                else:
                    pass
            else:
                if travel_option:
                    YPMerchantPageMap.cycling_is_success = True
                else:
                    pass
            count += 1

    def testing_travel_options(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.travel_options(link)
        if YPMerchantPageMap.driving_is_success:
            print("--> Test case is for \"Driving\" successful.")
        else:
            print("--> Test case is for \"Driving\" unsuccessful.")
        if YPMerchantPageMap.walking_is_success:
            print("--> Test case is for \"Walking\" successful.")
        else:
            print("--> Test case is for \"Walking\" unsuccessful.")
        if YPMerchantPageMap.cycling_is_success:
            print("--> Test case is for \"Cycling\" successful.")
        else:
            print("--> Test case is for \"Cycling\" unsuccessful.")


test = YPMerchantPageMap(driver)
test.testing_travel_options(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_travel_options(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
