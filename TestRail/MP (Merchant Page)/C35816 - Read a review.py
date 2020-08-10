import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPReadReview:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def read_a_review(self):
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

        # Locating the Read a review toggle
        read_a_review_toggle = My.search_presence_webelement(
            container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/a")
        if read_a_review_toggle:
            read_a_review_toggle.click()
            YPReadReview.is_success = True
            pass
        else:
            return

    def testing_read_a_review(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.read_a_review()
        if YPReadReview.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPReadReview(driver)
test.testing_read_a_review(My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
driver.quit()
sys.exit()
