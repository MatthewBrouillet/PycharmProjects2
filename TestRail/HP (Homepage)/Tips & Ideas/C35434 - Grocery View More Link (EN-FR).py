import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPTipsAndIdeas:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def tips_ideas_grocery_view_more(self, link):
        """
        >> This function verifies if the "View more" link of "Grocery" in the Tips & Ideas' section is clickable
        >> and leads to "https://www.yellowpages.ca/tips/cat/food-beverage/grocery-tips/" or
        >> "https://www.pagesjaunes.ca/trucs/cat/aliments-boissons/epicerie/"
        """
        # Locating the Tips and Ideas container
        tips_ideas_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]")

        if tips_ideas_container:
            cards_grid_grocery = My.search_presence_webelement(
                tips_ideas_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[2]/div")

            # Locating the View More link
            view_more_link = My.search_clickable_webelement(
                cards_grid_grocery, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[3]/div/div[3]/a")
            if view_more_link:
                view_more_link.click()
            else:
                return

            # Validating the URL of the current web page
            if driver.current_url == link + "/tips/cat/food-beverage/grocery-tips/":
                YPTipsAndIdeas.is_success = True
                return
            else:
                return

    def testing_tips_ideas_grocery_view_more(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.tips_ideas_grocery_view_more(link)
        if YPTipsAndIdeas.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPTipsAndIdeas(driver)
test.testing_tips_ideas_grocery_view_more(My.yp_web_link)
print('----------')
test.testing_tips_ideas_grocery_view_more(My.pj_web_link)
driver.quit()
sys.exit()
