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

    def app_store(self):
        """
        >> This function verifies that the App Store button is clickable and functional.
        """
        # Locating the Mobile App container
        mobile_app_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]')
        if mobile_app_container:
            pass
        else:
            return

        # Locating the App Store button
        app_store_button = My.search_clickable_webelement(
            mobile_app_container, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]/div/div[2]/ul/li[1]/a')
        if app_store_button:
            app_store_button.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == 'https://apps.apple.com/CA/app/id322964940?mt=8':
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_app_store(self, link):
        My.search_merchant_page(driver, link)
        test.app_store()
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_app_store(My.c411_qa_web_link)
