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

    def advertisers_quick_links(self, link):
        """
        >> This function verifies if the "Advertisers" quick links are clickable and functional
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
        if footer_container:
            pass
        else:
            return

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[2]/li[2]/a")
        if quick_link:
            quick_link.click()
        else:
            pass

        # Validating the URL of the current web page
        if driver.current_url == "https://www.yellowpages360solution.ca/en/index.htm":
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_advertisers_quick_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.advertisers_quick_links(link)
        if Canada411Home.is_success:
            print("-->> Test case for \"Advertisers\" is successful!")
        else:
            print("-->> Test case for \"Advertisers\" is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_advertisers_quick_links(My.c411_qa_web_link)
