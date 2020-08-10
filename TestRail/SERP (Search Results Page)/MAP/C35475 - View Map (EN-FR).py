import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPViewMap:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def view_map(self, link):
        """
        >> This function verifies if clicking the View Map on the MAP
        >> of the SERP page redirects you to the close-up version of the map.
        """
        # Locating the map
        map = My.search_presence_webelement(driver, By.ID, "ypgmap")
        if map:
            pass
        else:
            return

        # Locating the View Map button
        view_map_button = My.search_clickable_webelement(
            map, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/div[1]/aside/ul/li/a")
        if view_map_button:
            view_map_button.click()
            pass
        else:
            return

        # Locating the close up map
        map_closeup = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypgmap"]')
        if map_closeup:
            YPViewMap.is_success = True
            return
        else:
            return

    def testing_view_map(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.view_map(link)
        if YPViewMap.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPViewMap(driver)
test.testing_view_map(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_view_map(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
