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

    def tips_ideas_grocery_links(self):
        """
        >> This function verifies if the first link of "Grocery" in the Tips & Ideas' section is clickable
        """
        # Locating Tips and Ideas container
        tips_ideas_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]")

        if tips_ideas_container:
            cards_grid_grocery = My.search_presence_webelement(
                tips_ideas_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[2]/div")

            # Locating the first article link
            first_link = My.search_clickable_webelement(
                cards_grid_grocery, By.XPATH,
                "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[2]/h4/a")
            if first_link:
                first_link.click()
                YPTipsAndIdeas.is_success = True
            else:
                return

    def testing_tips_ideas_grocery_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.tips_ideas_grocery_links()
        if YPTipsAndIdeas.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPTipsAndIdeas(driver)
test.testing_tips_ideas_grocery_links(My.yp_web_link)
print('----------')
test.testing_tips_ideas_grocery_links(My.pj_web_link)
driver.quit()
sys.exit()
