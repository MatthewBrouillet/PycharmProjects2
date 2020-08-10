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

    def advertise_with_us(self):
        """
        >> This function verifies that the Advertise with us toggle is clickable and functional.
        """
        # Locating the Find a Business container
        find_a_business_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]')
        if find_a_business_container:
            pass
        else:
            return

        # Locating the More search options toggle
        advertise_with_us_toggle = My.search_clickable_webelement(
            find_a_business_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[4]/a')
        if advertise_with_us_toggle:
            advertise_with_us_toggle.click()
            pass
        else:
            return

        if driver.current_url == "https://www.yellowpages360solution.ca/en/index.htm":
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_advertise_with_us(self, link):
        My.search_merchant_page(driver, link)
        test.advertise_with_us()
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_advertise_with_us(My.c411_qa_web_link)
