import time

import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def write_a_review():
    """
    >> This function verifies if clicking the Write a Review button is clickable and functional.
    """
    # Locating the container
    container = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul")
    assert container

    # Locating the Write a Review button
    write_review = My.search_clickable_webelement(
        container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[2]/a")
    assert write_review
    write_review.click()

    time.sleep(5)

    # Locating the review popup window
    review = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgWriteReviewOverlay']/div/div")
    assert review


def testing_write_a_review():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
    write_a_review()
    driver.quit()
