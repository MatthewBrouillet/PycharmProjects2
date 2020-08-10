import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPLogin:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def validate_login(self):
        """
        >> This function verifies if the login pop-up window opens
        """
        # Locating the button on the top navigation bar
        button_login = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[5]")
        if button_login:
            button_login.click()
            pass
        else:
            return

        # Validating that the pop up window is present
        if My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypModal']/div/div"):
            YPLogin.is_success = True
            return
        else:
            return

    def testing_login(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.validate_login()
        if YPLogin.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPLogin(driver)
test.testing_login(My.yp_web_link)
print('----------')
test.testing_login(My.pj_web_link)
driver.quit()
sys.exit()
