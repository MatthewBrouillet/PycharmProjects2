import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWhereCLearAll:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def clear_previous_searches(self, link):
        """
        >> This function verifies the functionality of the "Clear all" toggle in the "where" box
        """
        # Sending keys to the WHAT and WHERE fields
        try:
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("dentist")
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='where']").send_keys("montreal")
            My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
        except:
            return

        # Waiting for the page to load
        target_page = WebDriverWait(driver, 20).until(ec.url_to_be(
            link + "/search/si/1/dentist/Montreal+QC"))

        # Locating the YP home button
        yp_home = My.search_presence_webelement(driver, By.ID, "QAypLogoLhs")
        if yp_home and target_page:
            yp_home.click()
        else:
            return

        # Locating the WHERE field
        where_box = My.search_presence_webelement(driver, By.ID, "where")
        if where_box:
            where_box.click()
        else:
            return

        # Locating the Clear All toggle
        clear_all = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='previousLocation']/h2/span[2]")
        if clear_all:
            clear_all.click()
        else:
            return

        # Clearing all the previous searches
        clear_message = My.search_presence_webelement(driver, By.XPATH, "//*[@id='previousLocation']/p")
        if clear_message and clear_message.get_attribute("textContent") == "Your recent locations have been cleared":
            YPWhereCLearAll.is_success = True
            return
        else:
            return

    def testing_clear_previous_searches(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.clear_previous_searches(link)
        if YPWhereCLearAll.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPWhereCLearAll(driver)
test.testing_clear_previous_searches(My.yp_web_link)
print('----------')
test.testing_clear_previous_searches(My.pj_web_link)
driver.quit()
sys.exit()
