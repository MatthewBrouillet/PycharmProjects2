import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPPrintOption:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success_EN = False
    is_success_FR = False

    def print_option_walking(self):
        """
        >> This function verifies if the print option is present and clickable.
        """
        # Locating the current location button
        current_location_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/form/div[2]/div[1]/span[3]")
        if current_location_button:
            current_location_button.click()
        else:
            return

        # Locating the Walking button
        walking_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/form/div[1]/ul/li[2]/a")
        if walking_button:
            walking_button.click()
            pass
        else:
            return

        # Locating the print button
        print_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/div/div[5]/button")
        if print_button:
            YPPrintOption.is_success_EN = True
            pass
        else:
            return

        # Locating the FR language toggle
        fr_toggle = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[2]/a")
        if fr_toggle:
            fr_toggle.click()
            pass
        else:
            return

        # Locating the current location button
        current_location_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/form/div[2]/div[1]/span[3]")
        if current_location_button:
            current_location_button.click()
        else:
            return

        # Locating the Walking button
        walking_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/form/div[1]/ul/li[2]/a")
        if walking_button:
            walking_button.click()
            pass
        else:
            return

        # Locating the print button
        print_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/div/div[5]/button")
        if print_button:
            YPPrintOption.is_success_FR = True
            return
        else:
            return

    def testing_print_option_walking(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.print_option_walking()
        if YPPrintOption.is_success_EN:
            print("--> Test case is for \"EN\" successful.")
        else:
            print("--> Test case is for \"EN\" unsuccessful.")
        if YPPrintOption.is_success_FR:
            print("--> Test case is for \"FR\" successful.")
        else:
            print("--> Test case is for \"FR\" unsuccessful.")
        driver.quit()
        sys.exit()


test = YPPrintOption(driver)
test.testing_print_option_walking(My.yp_web_link + "/merchant/directions/1329952")
