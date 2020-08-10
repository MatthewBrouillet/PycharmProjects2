import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class Canada411Home:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def drop_down_menu(self, link):
        """
        >> This function verifies that the search results are valid in regards to the keywords
        """
        # Locating the action bar
        action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
        if action_bar:
            pass
        else:
            return

        drop_down_menu = My.search_clickable_webelement(
            action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[1]/a')
        if drop_down_menu:
            drop_down_menu.click()
            pass
        else:
            return

        side_menu = My.search_presence_webelement(driver, By.XPATH, '/html/body/div[4]')
        if side_menu:
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_drop_down_menu(self, link):
        My.search_merchant_page(driver, link)
        test.drop_down_menu(link)
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_drop_down_menu(My.c411_qa_web_link)
