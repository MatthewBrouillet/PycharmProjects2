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

    def in_map_listing_card(self):
        """
        >> This function verifies if the "Merchant Card", when clicked, leads to the Merchant page
        """
        # Locating the entire search result container (map)
        map_results = My.search_presence_webelement(driver, By.ID, "ypgmap")

        # Locating the individual search results
        merchant_card = My.search_presence_webelement(
            map_results, By.XPATH, "//*[@id='ypgBody']/div[2]/div[3]/div[2]/div[2]/div")

        # Locating link to merchant page
        if merchant_card:
            link_to_merchant_page = My.search_clickable_webelement(
                merchant_card, By.XPATH,
                "//*[@id='ypgBody']/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/a")

            if link_to_merchant_page:
                link_to_merchant_page.click()
                YPDiscover.is_success = True
            else:
                return
        else:
            return

    def testing_in_map_listing_card(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.in_map_listing_card()
        if YPDiscover.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPDiscover(driver)
test.testing_in_map_listing_card(My.yp_web_link)
print('----------')
test.testing_in_map_listing_card(My.pj_web_link)
driver.quit()
sys.exit()
