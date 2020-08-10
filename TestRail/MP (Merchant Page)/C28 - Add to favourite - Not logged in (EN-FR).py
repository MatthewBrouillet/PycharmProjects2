import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPFavourites:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def add_to_favourites(self):
        """
        >> This function verifies if clicking on 'Add to favourites' is clickable and functional.
        """
        first_merchant_card = My.search_clickable_webelement(
            driver, By.TAG_NAME, "h3")
        if first_merchant_card:
            first_merchant_card.click()
            pass
        else:
            return

        add_to_favourites_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[1]/a")
        if add_to_favourites_button:
            add_to_favourites_button.click()
            pass
        else:
            return

        connect_with_yp_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypModal"]/div/div')
        if connect_with_yp_container:
            YPFavourites.is_success = True
            return
        else:
            return

    def testing_add_to_favourites(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.add_to_favourites()
        if YPFavourites.is_success:
            print("--> Test case for \"Add to favourites\" is successful.")
        else:
            print("--> Test case for \"Add to favourites\" is unsuccessful.")


test = YPFavourites(driver)
test.testing_add_to_favourites(My.yp_web_link + "/search/si/1/restaurants/Montreal+QC")
print('----------')
test.testing_add_to_favourites(My.pj_web_link + "/search/si/1/restaurants/Montreal+QC")
driver.quit()
sys.exit()
