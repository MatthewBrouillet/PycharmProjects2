import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPHomeButton:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def yp_home(self, link):
        """
        >> This function verifies if the PJ Home logo in the footer section is clickable
        >> and leads to yp.ca or pj.ca home page
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[2]")

        # Locating the YP home button
        if footer_container:
            yp_home_button = My.search_clickable_webelement(
                footer_container, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[1]/div[1]/a/span")

            if yp_home_button:
                yp_home_button.click()
            else:
                return
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link + "/":
            YPHomeButton.is_success = True
            return
        else:
            return

    def testing_yp_home(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.yp_home(link)
        if YPHomeButton.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPHomeButton(driver)
test.testing_yp_home(My.yp_web_link)
print('----------')
test.testing_yp_home(My.pj_web_link)
driver.quit()
sys.exit()
