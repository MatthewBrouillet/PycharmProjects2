import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPOpeningHours:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def opening_hours(self):
        """
        >> This function verifies if the opening hours of the merchant are displayed on the merchant card.
        """
        # Locating the Opening hours of the merchant
        hours = My.search_presence_webelement(
            driver, By.XPATH,
            '//*[@id="ypgBody"]/div[2]/div/div[1]/div[9]/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/a')
        if hours:
            print(str(hours.text))
            YPOpeningHours.is_success = True
            pass
        else:
            return

    def testing_opening_hours(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.opening_hours()
        if YPOpeningHours.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPOpeningHours(driver)
test.testing_opening_hours(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_opening_hours(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
