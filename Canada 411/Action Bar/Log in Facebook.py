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

    def log_in_facebook(self, link):
        """
        >> This function verifies that the language toggle is clickable and functional.
        """
        # Locating the action bar
        action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
        if action_bar:
            pass
        else:
            return

        log_in_toggle = My.search_clickable_webelement(
            action_bar, By.ID, 'c411YidLogin')
        if log_in_toggle:
            log_in_toggle.click()
            Canada411Home.is_success = True
            pass
        else:
            return

    def testing_log_in_facebook(self, link):
        My.search_merchant_page(driver, link)
        test.log_in_facebook(link)
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_log_in_facebook(My.c411_qa_web_link)
