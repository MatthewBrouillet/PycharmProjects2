import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPReviewStarsRatingCount:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success_write_review = False
    is_success_rating_count = False

    def review_stars_rating_count(self):
        """
        >> This function verifies if clicking the yellow rating stars on a Merchant Card
        >> redirects you to the reviews section of the MP where "Write a review" is visible
        """
        review_stars = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/a")
        if review_stars:
            review_stars.click()
            pass
        else:
            return

        ratings_and_reviews_container = My.search_clickable_webelement(driver, By.ID, "ypgReviewsHeader")
        if ratings_and_reviews_container:
            if My.search_visibility_webelement(
                    ratings_and_reviews_container, By.XPATH, "//*[@id='ypgReviewsHeader']/div[1]/div/a"):
                YPReviewStarsRatingCount.is_success_write_review = True
                pass
            else:
                pass
        else:
            return

        rating_count = My.search_clickable_webelement(
            ratings_and_reviews_container, By.XPATH, "//*[@id='reviewPreview']/nav/ul/li/a")

        if rating_count:
            try:
                webdriver.ActionChains(driver).move_to_element(rating_count).click(rating_count).perform()
            except:
                return
            YPReviewStarsRatingCount.is_success_rating_count = True
            return
        else:
            return

    def testing_review_stars_rating_count(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.review_stars_rating_count()
        if YPReviewStarsRatingCount.is_success_write_review:
            print("--> Test case for \"Write A Review\" is successful.")
        else:
            print("--> Test case for \"Write A Review\" is unsuccessful.")
        if YPReviewStarsRatingCount.is_success_rating_count:
            print("--> Test case for \"rating count\" is successful.")
        else:
            print("--> Test case for \"rating count\" is unsuccessful.")


test = YPReviewStarsRatingCount(driver)
test.testing_review_stars_rating_count(My.yp_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918.html")
print('----------')
test.testing_review_stars_rating_count(My.pj_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918.html")
driver.quit()
sys.exit()
