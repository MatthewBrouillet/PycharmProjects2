import sys
import time

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
    is_success_FR = False
    is_success_EN = False

    def lang_toggle(self, link_FR, link_EN):
        """
        >> This function verifies that the language toggles are clickable and functional.
        """
        # Locating the action bar
        action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
        if action_bar:
            pass
        else:
            return

        # Locating the language toggle
        lang_toggle = My.search_clickable_webelement(
            action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[2]/ul/li[5]/span')
        if lang_toggle:
            lang_toggle.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        print(str(driver.current_url))
        if driver.current_url == link_FR:
            Canada411Home.is_success_FR = True
            pass
        else:
            return

        time.sleep(5)

        # Locating the action bar
        action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
        if action_bar:
            pass
        else:
            return

        # Locating the language toggle
        lang_toggle = My.search_clickable_webelement(
            action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[2]/ul/li[5]/span')
        if lang_toggle:
            lang_toggle.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        print(str(driver.current_url))
        if driver.current_url == link_EN:
            Canada411Home.is_success_EN = True
            return
        else:
            return

    def testing_lang_toggle(self, link, link_FR, link_EN):
        My.search_merchant_page(driver, link)
        test.lang_toggle(link_FR, link_EN)
        if Canada411Home.is_success_FR:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        if Canada411Home.is_success_EN:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_lang_toggle(My.c411_qa_web_link, My.c411_fr_qa_web_link, 'http://www.qa.ui.mtl.canada411.ca/')
