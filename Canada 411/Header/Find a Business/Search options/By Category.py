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

    def by_category_link(self):
        """
        >> This function verifies that the By category toggle is clickable and functional.
        """
        # Locating the Find a Business container
        find_a_business_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]')
        if find_a_business_container:
            pass
        else:
            return

        # Locating the More search options toggle
        more_search_options_toggle = My.search_clickable_webelement(
            find_a_business_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/a')
        if more_search_options_toggle:
            more_search_options_toggle.click()
            pass
        else:
            return

        # Locating the By category link
        by_category = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[2]/div/ul/li[2]/ul/li[4]/a')
        if by_category:
            by_category.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        print(str(driver.current_url))
        if driver.current_url == 'https://canada411.yellowpages.ca/business/':
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_by_category_link(self, link):
        My.search_merchant_page(driver, link)
        test.by_category_link()
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_by_category_link(My.c411_qa_web_link)
