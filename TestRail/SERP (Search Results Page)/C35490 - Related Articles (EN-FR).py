import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPRelatedArticles:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def related_articles(self):
        """
        >> This function verifies if the first article of the 'Related Articles' is clickable and functional
        """
        # Locating the container
        container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/div[2]")

        # Locating the Related Articles button
        if container:
            related_articles_button = My.search_clickable_webelement(
                container, By.XPATH,
                "//*[@id='ypgBody']/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/a")
            if related_articles_button:
                related_articles_button.click()
                YPRelatedArticles.is_success = True
                return
            else:
                return
        else:
            return

    def testing_related_articles(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.related_articles()
        if YPRelatedArticles.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPRelatedArticles(driver)
test.testing_related_articles(My.yp_web_link + '/search/si/1/restaurants/Montreal+QC')
print('----------')
test.testing_related_articles(My.pj_web_link + '/search/si/1/restaurants/Montreal+QC')
driver.quit()
sys.exit()
