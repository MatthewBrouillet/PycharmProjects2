import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPReview:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def write_a_review(self):
        """
        >> This function verifies if clicking the Write a Review button is clickable and functional.
        """
        # Locating the container
        container = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul")
        if container:
            pass
        else:
            return

        # Locating the Write a Review button
        write_review = My.search_clickable_webelement(
            container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[2]/a")
        if write_review:
            write_review.click()
            pass
        else:
            return

        # Locating the review popup window
        review = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgWriteReviewOverlay']/div/div")
        if review:
            YPReview.is_success = True
            return
        else:
            return

    def testing_write_a_review(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.write_a_review()
        if YPReview.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPReview(driver)
test.testing_write_a_review(My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
driver.quit()
sys.exit()
