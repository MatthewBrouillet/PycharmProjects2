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
    mobile_tools_more_is_success = False
    shopwise_is_success = False

    def mobile_tools_more_quick_links(self):
        """
        >> This function verifies if the "Mobile, tools and more" quick links are clickable and functional
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
        if footer_container:
            pass
        else:
            return

        count = 1
        while count < 3:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[2]/li[" + str(count + 3) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                print(str(driver.current_url))
                if driver.current_url == "https://www.yellowpages.ca/applications/":
                    Canada411Home.mobile_tools_more_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                print(str(driver.current_url))
                if driver.current_url == "https://shopwise.yp.ca/":
                    Canada411Home.shopwise_is_success = True
                    pass
                else:
                    pass
            count += 1
            driver.back()

    def testing_mobile_tools_more_quick_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.mobile_tools_more_quick_links()
        if Canada411Home.mobile_tools_more_is_success:
            print("-->> Test case for \"Mobile, tools and more\" is successful!")
        else:
            print("-->> Test case for \"Mobile, tools and more\" is unsuccessful!")
        if Canada411Home.shopwise_is_success:
            print("-->> Test case for \"Shopwise\" is successful!")
        else:
            print("-->> Test case for \"Shopwise\" is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_mobile_tools_more_quick_links(My.c411_qa_web_link)
