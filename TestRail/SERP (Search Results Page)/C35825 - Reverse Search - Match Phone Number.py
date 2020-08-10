import sys
import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YellowPages:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False
    results_phone, results_header, results_failure = [], [], []
    page_count = 1

    def is_valid_search(self):
        """
        >> This function verifies if the search results are relevant to the entered key (in this case, phone number)
        """
        # Locating all individual result containers on the page
        containers = My.search_presence_webelements(driver, By.CLASS_NAME, "listing_right_section")

        for i in containers:
            header = My.search_presence_webelement(i, By.TAG_NAME, "a").text
            phone = My.search_presence_webelement(i, By.TAG_NAME, "h4").get_attribute('textContent')
            YellowPages.results_header.append(header)
            YellowPages.results_phone.append(phone)

        # Verifying the validity of the results
        if YellowPages.results_phone is None:
            return
        for phone in YellowPages.results_phone:
            if phone == '514-848-2424':
                pass
            else:
                YellowPages.results_failure.append(phone)

        # Locating the "Next" button
        if YellowPages.page_count == 1:
            has_next_page = My.search_presence_webelement(
                driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[7]/div[2]/a")
        else:
            has_next_page = My.search_presence_webelement(
                driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[7]/div[2]/a[2]")

        if bool(has_next_page):
            has_next_page.click()
            YellowPages.page_count += 1
            return self.is_valid_search()
        else:
            if not YellowPages.results_failure:
                YellowPages.is_success = True
                return
            else:
                print("List of failed results: " + str(YellowPages.results_failure))
                return

    def testing_phone_numbers(self, link, what, where):
        """
        >> This function will execute the test case, and takes a link, a phone number and a location as parameters
        """
        My.search_merchant_param(driver, link, what, where)
        test.is_valid_search()
        if YellowPages.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = YellowPages(driver)
test.testing_phone_numbers(My.qa_web_link, "5148482424", "Toronto")
# test.testing_phone_numbers(My.yp_web_link, "5148482424", "Toronto")
