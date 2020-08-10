import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPBusiness:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def business_discover_more(self):
        """
        >> This function verifies if the "Discover More" button is clickable
        >> and leads to "https://business.yellowpages.ca/home/#/"
        """
        # Locating the Discover More container
        container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[1]")

        # Locating the Discover More button
        if container:
            discover_more_button = My.search_clickable_webelement(
                container, By.XPATH, "//*[@id='ypgFooter']/div[1]/div[1]/a/div")
            if discover_more_button:
                discover_more_button.click()
            else:
                return
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == "https://business.yellowpages.ca/home/#/":
            YPBusiness.is_success = True
            return
        else:
            return

    def testing_business_discover_more(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.business_discover_more()
        if YPBusiness.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPBusiness(driver)
test.testing_business_discover_more(My.yp_web_link)
print('----------')
test.testing_business_discover_more(My.pj_web_link)
driver.quit()
sys.exit()
