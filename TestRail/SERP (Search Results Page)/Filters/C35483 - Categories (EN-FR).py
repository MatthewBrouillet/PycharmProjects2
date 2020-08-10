import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPCategories:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def nbr_search_results(self):
        """
        >> This function verifies if the Categories drop down menu is clickable and functional
        """
        # Locating the Categories button
        categories_button = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/ul[2]/li/a")
        if categories_button:
            categories_button.click()
            pass
        else:
            return

        # Locating the drop down menu
        drop_down_menu = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="ypgBody"]/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/ul[2]/li/div')
        if drop_down_menu:
            YPCategories.is_success = True
            return
        else:
            return

    def testing_nbr_search_results(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.nbr_search_results()
        if YPCategories.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPCategories(driver)
test.testing_nbr_search_results(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_nbr_search_results(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
