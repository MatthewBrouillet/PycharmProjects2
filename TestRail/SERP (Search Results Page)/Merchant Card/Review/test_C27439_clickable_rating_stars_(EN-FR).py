import time

import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def review_stars():
    """
    >> This function verifies if clicking the yellow rating stars on a Merchant Card
    >> redirects you to the reviews section of the MP
    """
    # Locating the search results
    search_results = My.search_presence_webelement(driver, By.CLASS_NAME, "page__container_wrap")
    assert search_results

    driver.implicitly_wait(5)

    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(search_results, By.XPATH, "//div//div//div//div//div")
    assert first_merchant_card

    # Locating the rating stars of the merchant
    rating_stars = My.search_clickable_webelement(
        first_merchant_card, By.XPATH, "//div//div//div[2]//div//div[2]//div//div//div//a")
    if rating_stars:
        assert rating_stars
        rating_stars.click()
    else:
        print("This merchant card does not have a trip advisor review")
        return

    driver.implicitly_wait(5)

    # Locating the Ratings and Review container
    ratings_and_reviews_container = My.search_presence_webelement(driver, By.ID, "ypgReviewsHeader")
    assert ratings_and_reviews_container

    review_details = My.search_visibility_webelement(ratings_and_reviews_container, By.ID, "reviewDetails_yp")
    assert review_details


def test_review_stars():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    review_stars()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    review_stars()
    driver.quit()
