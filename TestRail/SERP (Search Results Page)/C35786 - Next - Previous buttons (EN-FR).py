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
    is_success_next = False
    is_success_previous = False

    def next_previous(self):
        """
        >> This function verifies if the next and previous buttons are clickable and functional.
        """
        # Locating the next button
        next_button = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[9]/div[2]/a")
        if next_button:
            next_button.click()
            YPMerchantCardLinks.is_success_next = True
            pass
        else:
            return

        # Locating the previous button
        previous_button = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[9]/div[2]/a[1]")
        if previous_button:
            previous_button.click()
            YPMerchantCardLinks.is_success_previous = True
            pass
        else:
            return

    def testing_next_previous(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.next_previous()
        if YPMerchantCardLinks.is_success_next:
            print("--> Test case for \"Next\" is successful.")
        else:
            print("--> Test case for \"Next\" is unsuccessful.")
        if YPMerchantCardLinks.is_success_previous:
            print("--> Test case for \"Previous\" is successful.")
        else:
            print("--> Test case for \"Previous\" is unsuccessful.")


test = YPMerchantCardLinks(driver)
test.testing_next_previous(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_next_previous(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
