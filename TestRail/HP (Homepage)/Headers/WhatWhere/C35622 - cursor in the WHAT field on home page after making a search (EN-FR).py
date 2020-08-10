import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWhat:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def cursor_default_back(self, link):
        """
        >> This function verifies if the default position of the cursor is on the WHAT box
        >> when you go back to the home page after making a search.
        """
        # Validating that the the active element (cursor) is in the WHAT field
        if driver.switch_to.active_element == My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']"):
            pass
        else:
            return

        # Sending keys to the "WHAT" and "WHERE" fields
        try:
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("restaurants")
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='where']").send_keys("montreal")
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
        except:
            return

        # Waiting for the result page to load
        target_page = WebDriverWait(driver, 20).until(ec.url_to_be(
            link + "/search/si/1/restaurants/Montreal+QC"))

        # Clicking the YP Home button to go back to the home page
        yp_home = My.search_presence_webelement(driver, By.ID, "QAypLogoLhs")
        if yp_home and target_page:
            yp_home.click()
        else:
            return

        # Validating that the the active element (cursor) is in the WHAT field
        if driver.switch_to.active_element == My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']"):
            YPWhat.is_success = True
            return
        else:
            return

    def testing_cursor_default_back(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.cursor_default_back(link)
        if YPWhat.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPWhat(driver)
test.testing_cursor_default_back(My.yp_web_link)
print('----------')
test.testing_cursor_default_back(My.pj_web_link)
driver.quit()
sys.exit()
