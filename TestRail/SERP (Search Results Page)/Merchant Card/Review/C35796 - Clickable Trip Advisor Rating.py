import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPReviewStars:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def trip_advisor(self):
        """
        >> This function verifies if clicking the yellow rating stars on a Merchant Card
        >> redirects you to the Trip Advisor section of the MP
        """
        # Locating the search results
        search_results = My.search_presence_webelement(driver, By.CLASS_NAME, "page__container_wrap")
        if search_results:
            pass
        else:
            return

        # Locating the first merchant card
        first_merchant_card = My.search_presence_webelement(
            search_results, By.XPATH, "//div//div//div//div//div")
        if first_merchant_card:
            pass
        else:
            return

        # Locating the trip advisor rating of the merchant
        rating_stars = My.search_clickable_webelement(
            first_merchant_card, By.XPATH, "//div//div//div[2]//div//div[2]//div//div//div[2]//a")

        if rating_stars:
            rating_stars.click()
            pass
        else:
            return

        # Locating the Ratings and Review container
        ratings_and_reviews_container = My.search_presence_webelement(driver, By.ID, "ypgReviewsHeader")
        if ratings_and_reviews_container:
            if My.search_visibility_webelement(
                    ratings_and_reviews_container, By.ID, "reviewDetails_ta"):
                YPReviewStars.is_success = True
                return
            else:
                return
        else:
            return

    def testing_trip_advisor(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.trip_advisor()
        if YPReviewStars.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPReviewStars(driver)
test.testing_trip_advisor(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_trip_advisor(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
