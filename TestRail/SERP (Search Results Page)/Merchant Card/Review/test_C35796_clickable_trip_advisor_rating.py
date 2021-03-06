import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def trip_advisor():
    """
    >> This function verifies if clicking the yellow rating stars on a Merchant Card
    >> redirects you to the Trip Advisor section of the MP
    """
    # Locating the search results
    search_results = My.search_presence_webelement(driver, By.CLASS_NAME, "page__container_wrap")
    assert search_results

    driver.implicitly_wait(5)

    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(search_results, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Locating the trip advisor rating of the merchant
    rating_stars = My.search_clickable_webelement(
        first_merchant_card, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[9]/div[1]/div[2]/div"
        "/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/a/img")
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

    review_details = My.search_clickable_webelement(
        ratings_and_reviews_container, By.CSS_SELECTOR, "#reviewPreview > nav > ul "
                                              "> li.hide-print.reviews-tabs--item.reviews-tabs--ta.reviewTab_ta "
                                              "> a")
    assert review_details
    review_details.click()


def test_trip_advisor():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    trip_advisor()
    driver.quit()
