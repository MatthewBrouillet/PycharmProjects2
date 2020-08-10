import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPCurrentLocation:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def current_location(self):
        """
        >> This function verifies if clicking the current location button on the MAP
        >> of the SERP page.
        """
        # Locating the map
        map = My.search_presence_webelement(driver, By.ID, "ypgmap")
        if map:
            pass
        else:
            return

        # Locating the current location button
        current_location = My.search_clickable_webelement(
            map, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[2]/a")
        if current_location:
            current_location.click()
            pass
        else:
            return

        YPCurrentLocation.is_success = True

    def testing_current_location(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.current_location()
        if YPCurrentLocation.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPCurrentLocation(driver)
test.testing_current_location(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_current_location(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
