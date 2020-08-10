import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPShare:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def share(self):
        """
        >> This function verifies if clicking the Share button is clickable and functional.
        """
        # Locating the container
        container = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul")
        if container:
            pass
        else:
            return

        # Locating the Share button
        share_button = My.search_clickable_webelement(
            container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[3]")
        if share_button:
            share_button.click()
            pass
        else:
            return

        # Locating the share drop down menu
        share_drop_down = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[3]/ul")
        if share_drop_down:
            YPShare.is_success = True
            return
        else:
            return

    def testing_share(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.share()
        if YPShare.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPShare(driver)
test.testing_share(My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
driver.quit()
sys.exit()
