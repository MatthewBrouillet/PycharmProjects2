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

    def more_search_options_toggle(self):
        """
        >> This function verifies that the More search options toggle is clickable and functional.
        """
        # Locating the Find a Person container
        find_a_person_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]')
        if find_a_person_container:
            pass
        else:
            return

        # Locating the More search options toggle
        more_search_options_toggle = My.search_clickable_webelement(
            find_a_person_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/a')
        if more_search_options_toggle:
            more_search_options_toggle.click()
            pass
        else:
            return

        # Locating the drop down menu
        drop_down_menu = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul')
        if drop_down_menu:
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_more_search_options_toggle(self, link):
        My.search_merchant_page(driver, link)
        test.more_search_options_toggle()
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_more_search_options_toggle(My.c411_qa_web_link)
