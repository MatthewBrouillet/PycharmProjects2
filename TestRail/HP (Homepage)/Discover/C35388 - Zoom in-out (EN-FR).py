import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMapZoomInZoomOut:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    zoom_in_is_success = False
    zoom_out_is_success = False

    def has_zoom_in_out(self):
        """
        >> This function verifies if the "+" (Zoom in) button and the "-" (Zoom out) button on the map are functional
        """
        # Locating the entire search result container (map)
        map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")

        # Locating zoom-in and zoom-out buttons
        if map_results:
            zoom_in_button = My.search_clickable_webelement(map_results, By.XPATH,
                                                            "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[1]")
            zoom_out_button = My.search_clickable_webelement(map_results, By.XPATH,
                                                             "//*[@id='ypgmap']/div[2]/div[1]/div[1]/a[2]")
            if zoom_in_button:
                try:
                    zoom_in_button.click()
                    YPMapZoomInZoomOut.zoom_in_is_success = True
                except:
                    return
            else:
                return
            if zoom_out_button:
                try:
                    zoom_out_button.click()
                    YPMapZoomInZoomOut.zoom_out_is_success = True
                except:
                    return
            else:
                return
        else:
            return

    def testing_has_zoom_in_out(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.has_zoom_in_out()
        if YPMapZoomInZoomOut.zoom_in_is_success:
            print("-->> Test case for \"Zoom in\" is successful!")
        else:
            print("-->> Test case for \"Zoom in\" is unsuccessful!")
        if YPMapZoomInZoomOut.zoom_out_is_success:
            print("-->> Test case for \"Zoom out\" is successful!")
        else:
            print("-->> Test case for \"Zoom out\" is unsuccessful!")


test = YPMapZoomInZoomOut(driver)
test.testing_has_zoom_in_out(My.yp_web_link)
print('----------')
test.testing_has_zoom_in_out(My.pj_web_link)
driver.quit()
sys.exit()
