import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWhatDropDown:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def delete_previous_search(self, link):
        """
        >> This function verifies the functionality of the "X" (delete) toggle in the recent searches section
        """
        # Sending keys to the "WHAT" and "WHERE" fields
        try:
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("dentist")
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='where']").send_keys("montreal")
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
        except:
            return

        # Waiting for the result page to load
        target_page = WebDriverWait(driver, 20).until(ec.url_to_be(
            link + "/search/si/1/dentist/Montreal+QC"))

        # Clicking the YP Home button to go back to the home page
        yp_home = My.search_presence_webelement(driver, By.ID, "QAypLogoLhs")
        if yp_home and target_page:
            yp_home.click()
        else:
            return

        # Validating the previous search in the WHATH field, and using it to make a second search
        whatwho_box = My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']")
        if whatwho_box:
            whatwho_box.click()
            previous_search = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='previousSearchesDropdown']/div/div/div/ul")
            if previous_search:
                previous_search.click()
            else:
                return
            try:
                My.search_presence_webelement(driver, By.XPATH, "//*[@id='where']").send_keys("montreal")
                My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
            except:
                return
        else:
            return

        YPWhatDropDown.is_success = True

    def testing_delete_previous_search(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.delete_previous_search(link)
        if YPWhatDropDown.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPWhatDropDown(driver)
test.testing_delete_previous_search(My.yp_web_link)
print('----------')
test.testing_delete_previous_search(My.pj_web_link)
driver.quit()
sys.exit()
