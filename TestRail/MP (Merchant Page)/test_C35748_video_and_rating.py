import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def has_video_rating():
    """
    >> This function verifies if the Video and Rating of the merchant are displayed.
    """
    # Locating the rating stars
    rating_stars = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/a/span")
    assert rating_stars

    # Locating the media container
    media_container = My.search_presence_webelement(driver, By.CLASS_NAME, "multimedia")
    assert media_container

    # Locating the video
    video = My.search_clickable_webelement(
        media_container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/ul/li[1]/a")
    assert video
    video.click()


def testing_has_video_rating():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Alberta/Edmonton/Action-Moving-Storage/8076228.html")
    has_video_rating()
    driver.quit()
