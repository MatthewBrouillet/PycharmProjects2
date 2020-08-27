import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def review_stars_rating_count():
    """
    >> This function verifies if clicking the yellow rating stars on a Merchant Card
    >> redirects you to the reviews section of the MP where "Write a review" is visible
    """
    review_stars = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/a")
    assert review_stars
    review_stars.click()

    ratings_and_reviews_container = My.search_clickable_webelement(driver, By.ID, "ypgReviewsHeader")
    assert ratings_and_reviews_container

    write_review = My.search_visibility_webelement(
        ratings_and_reviews_container, By.XPATH, "//*[@id='ypgReviewsHeader']/div[1]/div/a")
    assert write_review

    rating_count = My.search_clickable_webelement(
        ratings_and_reviews_container, By.XPATH, "//*[@id='reviewPreview']/nav/ul/li/a")
    assert rating_count
    try:
        webdriver.ActionChains(driver).move_to_element(rating_count).click(rating_count).perform()
    except:
        return


def testing_review_stars_rating_count():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918.html")
    review_stars_rating_count()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918.html")
    review_stars_rating_count()
    driver.quit()
