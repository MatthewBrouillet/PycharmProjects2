import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPPrintOptionPopUp:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def print_popup(self):
        """
        >> This function verifies if the print option is present and clickable.
        """
        current_location_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/form/div[2]/div[1]/span[3]")
        if current_location_button:
            current_location_button.click()
        else:
            return

        print_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='DRIVING']/div/div[5]/button")
        if print_button:
            print('Print Button is clickable')
            # webdriver.ActionChains(driver).move_to_element(print_button).click(print_button).perform()
            # print_button.click()
            # driver.switch_to.alert().dismiss()
            YPPrintOptionPopUp.is_success = True
            return
        else:
            return

        # print_popup_window_cancel = My.search_presence_webelement(
        #     driver, By.XPATH, "//*[@id='button-strip']/ paper-button[2]")

        # if print_popup_window_cancel:
        #     print('hey')
        #     YPPrintOptionPopUp.is_success = True
        #     return
        # else:
        #     return

    def testing_print_popup(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.print_popup()
        if YPPrintOptionPopUp.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")
        driver.quit()
        sys.exit()


test = YPPrintOptionPopUp(driver)
test.testing_print_popup(My.yp_web_link + "/merchant/directions/1329952")
