import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPLang:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def validate(self, link):
        """
        >> This function verifies if, when you click on the EN / FR button,
        >> the page is redirected to yellowpages.ca / pagesjaunes.ca
        """
        # Locating the language toggle
        lang_toggle = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[6]/a")
        if lang_toggle:
            lang_toggle.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        if link == My.yp_web_link:
            if driver.current_url == My.pj_web_link + '/?theme=yellowpages':
                YPLang.is_success = True
                return
            else:
                return
        else:
            if driver.current_url == My.yp_web_link + '/?theme=yellowpages':
                YPLang.is_success = True
                return
            else:
                return

    def testing_validate(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.validate(link)
        if YPLang.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPLang(driver)
test.testing_validate(My.yp_web_link)
print('----------')
test.testing_validate(My.pj_web_link)
driver.quit()
sys.exit()
