import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPRateTheseResults:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def rate_these_results(self):
        """
        >> This function verifies if the Rate these results toggle is clickable and leads to a pop up window
        """
        # Locating the Rate these results toggle
        rate_these_results = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/a")
        if rate_these_results:
            rate_these_results.click()
            pass
        else:
            return

        # Locating the Rate these results pop-up window
        rate_pop_up = My.search_presence_webelement(
            rate_these_results, By.XPATH, "//*[@id='ypModaRateResult']/div/div")
        if rate_pop_up:
            YPRateTheseResults.is_success = True
            pass
        else:
            return

    def testing_rate_these_results(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.rate_these_results()
        if YPRateTheseResults.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPRateTheseResults(driver)
test.testing_rate_these_results(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_rate_these_results(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
