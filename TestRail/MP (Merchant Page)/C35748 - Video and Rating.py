import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPVideoandRating:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success_video = False
    is_success_rating = False

    def has_video_rating(self):
        """
        >> This function verifies if the Video and Rating of the merchant are displayed.
        """
        # Locating the rating stars
        rating_stars = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/a/span")
        if rating_stars:
            YPVideoandRating.is_success_rating = True
            pass
        else:
            pass

        # Locating the media container
        media_container = My.search_presence_webelement(driver, By.CLASS_NAME, "multimedia")
        if media_container:
            pass
        else:
            pass

        # Locating the video
        video = My.search_clickable_webelement(
            media_container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/ul/li[1]/a")
        if video:
            video.click()
            YPVideoandRating.is_success_video = True
            return
        else:
            return

    def testing_has_video_rating(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.has_video_rating()
        if YPVideoandRating.is_success_rating:
            print("--> Test case for \"Rating\" is successful.")
        else:
            print("--> Test case for \"Rating\" is unsuccessful.")
        if YPVideoandRating.is_success_video:
            print("--> Test case for \"Video\" is successful.")
        else:
            print("--> Test case for \"Video\" is unsuccessful.")


test = YPVideoandRating(driver)
test.testing_has_video_rating(My.qa_web_link + "/bus/Alberta/Edmonton/Action-Moving-Storage/8076228.html")
driver.quit()
sys.exit()
