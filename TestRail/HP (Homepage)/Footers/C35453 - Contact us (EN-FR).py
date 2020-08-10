import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPContactUS:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def contact_us(self, link):
        """
        >> This function verifies if the "Contact us" toggle is clickable
        >> and leads to "/contactus" or "/pournousjoindre"
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[2]")

        # Locating Contact us button
        if footer_container:
            contact_us_button = My.search_clickable_webelement(
                footer_container, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[1]/div[2]/a[1]")

            if contact_us_button:
                contact_us_button.click()
            else:
                return
        else:
            return

        # Switching to the new window
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        # Validating the URL of the current web page
        if link == My.yp_web_link:
            if driver.current_url == link + "/contactus":
                YPContactUS.is_success = True
                return
            else:
                return
        else:
            if driver.current_url == link + "/pournousjoindre":
                YPContactUS.is_success = True
                return
            else:
                return

    def testing_contact_us(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.contact_us(link)
        if YPContactUS.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPContactUS(driver)
test.testing_contact_us(My.yp_web_link)
print('----------')
test.testing_contact_us(My.pj_web_link)
driver.quit()
sys.exit()
