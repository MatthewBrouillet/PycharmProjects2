import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWhereCurrentLocation:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def where_current_location(self):
        """
        >> This function verifies the functionality of the "Current Location" toggle in the "where" drop down
        """
        # Sending keys to the WHAT and WHERE fields
        try:
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("dentist")
            My.search_presence_webelement(driver, By.ID, "where").click()

            # Selecting the current location option from the WHERE field
            current_location_button = My.search_clickable_webelement(driver, By.ID, "currentLocation")
            if current_location_button:
                current_location_button.click()
            else:
                return
        except:
            return

        YPWhereCurrentLocation.is_success = True

    def testing_where_current_location(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.where_current_location()
        if YPWhereCurrentLocation.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPWhereCurrentLocation(driver)
test.testing_where_current_location(My.yp_web_link)
print('----------')
test.testing_where_current_location(My.pj_web_link)
driver.quit()
sys.exit()
