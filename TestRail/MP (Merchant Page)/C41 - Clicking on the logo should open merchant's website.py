import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPLogo:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def merchant_logo(self):
        """
        >> This function verifies if clicking on the logo leads to the merchant page.
        """
        # Locating the rating stars
        merchant_logo = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[1]/div/a")
        if merchant_logo:
            merchant_logo.click()
            pass
        else:
            return

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        print(str(driver.current_url))
        if driver.current_url[0:25] == "http://www.chaletbbq.com/":
            YPLogo.is_success = True
            return
        else:
            return

    def testing_merchant_logo(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.merchant_logo()
        if YPLogo.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPLogo(driver)
test.testing_merchant_logo(My.yp_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
driver.quit()
sys.exit()
