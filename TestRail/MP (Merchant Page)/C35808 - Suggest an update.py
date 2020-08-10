import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPSuggestAnUpdate:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def suggest_an_update(self):
        """
        >> This function verifies if clicking the Suggest an Update button is clickable and functional.
        """
        # Locating the container
        container = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul")
        if container:
            pass
        else:
            return

        # Locating the Suggest an Update button
        suggest_an_update_button = My.search_clickable_webelement(
            container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[4]/button")
        if suggest_an_update_button:
            suggest_an_update_button.click()
            pass
        else:
            return

        # Locating the Suggest an Update popup window
        suggest_popup = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypSuggestUpdateOwner']/div/div")
        if suggest_popup:
            YPSuggestAnUpdate.is_success = True
            return
        else:
            return

    def testing_suggest_an_update(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.suggest_an_update()
        if YPSuggestAnUpdate.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPSuggestAnUpdate(driver)
test.testing_suggest_an_update(My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
driver.quit()
sys.exit()
