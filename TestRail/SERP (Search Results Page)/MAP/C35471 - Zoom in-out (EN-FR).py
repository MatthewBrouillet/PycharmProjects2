import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPZoomMap:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def zoom_in_out(self):
        """
        >> This function verifies if clicking the zoom-in and zoom-out buttons on the MAP
        >> of the SERP page.
        """
        # Locating the map
        map = My.search_presence_webelement(driver, By.ID, "ypgmap")
        if map:
            pass
        else:
            return

        # Locating the zoom-in button
        zoom_in_button = My.search_clickable_webelement(
            map, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[1]")
        if zoom_in_button:
            zoom_in_button.click()
            pass
        else:
            return

        # Locating the zoom-out button
        zoom_out_button = My.search_clickable_webelement(
            map, By.XPATH, "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[2]")
        if zoom_out_button:
            zoom_out_button.click()
            pass
        else:
            return

        YPZoomMap.is_success = True

    def testing_zoom_in_out(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.zoom_in_out()
        if YPZoomMap.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPZoomMap(driver)
test.testing_zoom_in_out(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_zoom_in_out(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
