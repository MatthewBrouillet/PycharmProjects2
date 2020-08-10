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
    is_success = False

    def map_push_pin(self):
        """
        >> This function verifies if the "Merchant Pins" on the map are clickable
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
            merchant_pin = My.search_clickable_webelement(
                i, By.XPATH, "//*[@id='ypgmap']/div[1]/div[4]/div[" + str(count) + "]/div")

            if merchant_pin:
                try:
                    webdriver.ActionChains(driver).move_to_element(merchant_pin).click(merchant_pin).perform()
                except:
                    return
            else:
                return
            count += 1

        YPDiscover.is_success = True
        return

    def testing_map_push_pin(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.map_push_pin()
        if YPDiscover.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPDiscover(driver)
test.testing_map_push_pin(My.yp_web_link)
print('----------')
test.testing_map_push_pin(My.pj_web_link)
driver.quit()
sys.exit()
