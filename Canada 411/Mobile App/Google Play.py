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

    def google_play(self):
        """
        >> This function verifies that the Google Play button is clickable and functional.
        """
        # Locating the Mobile App container
        mobile_app_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]')
        if mobile_app_container:
            pass
        else:
            return

        # Locating the Google Play button
        google_play_button = My.search_clickable_webelement(
            mobile_app_container, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]/div/div[2]/ul/li[2]/a')
        if google_play_button:
            google_play_button.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url[0:35] == "https://play.google.com/store/apps/":
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_google_play(self, link):
        My.search_merchant_page(driver, link)
        test.google_play()
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_google_play(My.c411_qa_web_link)
