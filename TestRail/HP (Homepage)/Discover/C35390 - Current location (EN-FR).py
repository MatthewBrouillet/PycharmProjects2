import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMapCurrentLocation:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def has_current_location(self):
        """
        >> This function verifies if the "Current Location" button on the map is functional
        """
        # Locating the entire search result container (map)
        map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")

        # Locating the current location button
        if map_results:
            current_location_button = My.search_clickable_webelement(map_results, By.XPATH,
                                                                     "//*[@id='ypgmap']/div[2]/div[1]/div[2]/a")
            if current_location_button:
                current_location_button.click()
                YPMapCurrentLocation.is_success = True
            else:
                return
        else:
            return

    def testing_has_current_location(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.has_current_location()
        if YPMapCurrentLocation.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPMapCurrentLocation(driver)
test.testing_has_current_location(My.yp_web_link)
print('----------')
test.testing_has_current_location(My.pj_web_link)
driver.quit()
sys.exit()
