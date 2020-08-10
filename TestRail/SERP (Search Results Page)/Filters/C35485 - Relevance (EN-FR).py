import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPRelevance:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False
    count = 2

    def relevance_click(self):
        relevance_button = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[1]/div/div/a")
        if relevance_button:
            relevance_button.click()
            pass
        else:
            return

    def relevance(self, link):
        """
        >> This function verifies if the Relevance drop down menu is clickable and functional.
        """
        while YPRelevance.count < 6:
            self.relevance_click()

            if YPRelevance.count == 1:
                if link[0:26] == My.yp_web_link:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Closest')
                else:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Plus proche')
            if YPRelevance.count == 2:
                if link[0:26] == My.yp_web_link:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Highest rated')
                else:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Mieux évalués')
            if YPRelevance.count == 3:
                if link[0:26] == My.yp_web_link:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Most reviewed')
                else:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Plus commentés')
            if YPRelevance.count == 4:
                if link[0:26] == My.yp_web_link:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Alphabetical')
                else:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Ordre alphabétique')
            if YPRelevance.count == 5:
                if link[0:26] == My.yp_web_link:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Recently Reviewed')
                else:
                    button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Avis récent')

            if button:
                button.click()
            else:
                return

            YPRelevance.count = YPRelevance.count + 1
            driver.back()
        YPRelevance.is_success = True

    def testing_relevance(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.relevance(link)
        if YPRelevance.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPRelevance(driver)
test.testing_relevance(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_relevance(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
