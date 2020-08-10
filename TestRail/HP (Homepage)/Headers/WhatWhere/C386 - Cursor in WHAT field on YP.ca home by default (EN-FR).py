import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWhat:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def cursor_what(self):
        """
        >> This function verifies if the default position of the cursor is on the WHAT box
        """
        # Validating that the the active element (cursor) is in the WHAT field
        if driver.switch_to.active_element == My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']"):
            YPWhat.is_success = True
            return
        else:
            return

    def testing_cursor_what(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.cursor_what()
        if YPWhat.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPWhat(driver)
test.testing_cursor_what(My.yp_web_link)
print('----------')
test.testing_cursor_what(My.pj_web_link)
driver.quit()
sys.exit()
