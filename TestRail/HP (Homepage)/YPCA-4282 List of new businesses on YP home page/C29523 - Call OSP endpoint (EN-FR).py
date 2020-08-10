import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPDiscover:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    map_displayed_is_success = False
    businesses_displayed_is_success = False

    def has_displayed_map_and_businesses(self):
        """
        >> This function verifies if the "Discover businesses in your area" map is displayed
        >> and if it displays businesses in area
        """
        count = 1

        # Locating the entire search result container (map)
        map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")
        if map_results.is_displayed():
            YPDiscover.map_displayed_is_success = True
        else:
            return

        # Locating the individual search results
        containers = My.search_presence_webelements(map_results, By.XPATH, "//div//div[4]")

        # Looping through every gas station
        for i in containers:

            # Verifying if the merchant link is located on the map and if it is clickable
            merchant_pin = My.search_presence_webelement(
                i, By.XPATH, "//*[@id='ypgmap']/div[1]/div[4]/div[" + str(count) + "]/div")
            if not merchant_pin:
                return
            count += 1

        YPDiscover.businesses_displayed_is_success = True
        return

    def testing_has_displayed_map_and_businesses(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.has_displayed_map_and_businesses()
        if YPDiscover.map_displayed_is_success:
            print("-->> Test case for \"displayed map\" is successful!")
        else:
            print("-->> Test case for \"displayed map\"  is unsuccessful!")
        if YPDiscover.businesses_displayed_is_success:
            print("-->> Test case for \"displayed businesses\" is successful!")
        else:
            print("-->> Test case for \"displayed businesses\"  is unsuccessful!")


test = YPDiscover(driver)
test.testing_has_displayed_map_and_businesses(My.yp_web_link)
print('----------')
test.testing_has_displayed_map_and_businesses(My.pj_web_link)
driver.quit()
sys.exit()
