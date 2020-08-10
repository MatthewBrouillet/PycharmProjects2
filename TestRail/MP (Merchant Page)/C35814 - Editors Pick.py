import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPEditorsPick:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def has_editors_pick(self):
        """
        >> This function verifies if the Editors Pick is present on the merchant page.
        """
        # Locating the container
        container = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]")
        if container:
            pass
        else:
            return

        # Locating the Editors Pick
        editors_pick = My.search_presence_webelement(
            container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/a")
        if editors_pick.is_displayed():
            YPEditorsPick.is_success = True
            pass
        else:
            return

    def testing_has_editors_pick(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.has_editors_pick()
        if YPEditorsPick.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPEditorsPick(driver)
test.testing_has_editors_pick(My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
driver.quit()
sys.exit()
