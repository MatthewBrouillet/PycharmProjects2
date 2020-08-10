import sys
import myModule as My
from selenium import webdriver

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWindowTitle:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success_EN = False
    is_success_FR = False

    def window_title(self, link):
        """
        >> This function verifies the window title for the "best" search results
        """
        # Locating the displayed text
        if link == My.yp_web_link + "/search/si/1/restaurants/Montreal+QC":
            if driver.title == "The Best restaurants in Montreal | YellowPages.ca™":
                YPWindowTitle.is_success_EN = True
            else:
                return
        else:
            if driver.title == "Les meilleur(e)s restaurants à Montréal | PagesJaunes.ca(MC)":
                YPWindowTitle.is_success_FR = True
            else:
                return

    def testing_window_title(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.window_title(link)
        if link == My.yp_web_link + "/search/si/1/restaurants/Montreal+QC":
            if YPWindowTitle.is_success_EN:
                print("--> Test case is successful.")
            else:
                print("--> Test case is unsuccessful.")
        else:
            if YPWindowTitle.is_success_FR:
                print("--> Test case is successful.")
            else:
                print("--> Test case is unsuccessful.")


test = YPWindowTitle(driver)
test.testing_window_title(My.yp_web_link + "/search/si/1/restaurants/Montreal+QC")
print('----------')
test.testing_window_title(My.pj_web_link + "/search/si/1/restaurants/Montreal+QC")
driver.quit()
sys.exit()
