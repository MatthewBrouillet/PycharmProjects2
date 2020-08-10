import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class Canada411Home:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def connect_with_facebook(self):
        """
        >> This function verifies that the Connect with Facebook button is clickable and functional.
        """
        # Locating the Social container
        social_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[2]')
        if social_container:
            pass
        else:
            return

        # Locating the Connect with Facebook button
        connect_with_facebook = My.search_clickable_webelement(
            social_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/a')
        if connect_with_facebook:
            connect_with_facebook.click()
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_connect_with_facebook(self, link):
        My.search_merchant_page(driver, link)
        test.connect_with_facebook()
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_connect_with_facebook(My.c411_qa_web_link)
