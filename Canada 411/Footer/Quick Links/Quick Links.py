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
    faq_is_success = False
    help_is_success = False
    dncl_is_success = False
    request_res_dir_is_success = False

    def quick_links(self, link):
        """
        >> This function verifies if the "Quick links" quick links are clickable and functional
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
        if footer_container:
            pass
        else:
            return

        count = 1
        while count < 5:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[3]/li[" + str(count + 1) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                # print(str(driver.current_url))
                if driver.current_url == link + "help.html?key=faq":
                    Canada411Home.faq_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                # print(str(driver.current_url))
                if driver.current_url == link + "help.html":
                    Canada411Home.help_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                # print(str(driver.current_url))
                if driver.current_url == "https://lnnte-dncl.gc.ca/":
                    Canada411Home.dncl_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                # print(str(driver.current_url))
                if driver.current_url == "https://delivery.yp.ca/":
                    Canada411Home.request_res_dir_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_quick_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.quick_links(link)
        if Canada411Home.faq_is_success:
            print("-->> Test case for \"FAQ\" is successful!")
        else:
            print("-->> Test case for \"FAQ\" is unsuccessful!")
        if Canada411Home.help_is_success:
            print("-->> Test case for \"Help\" is successful!")
        else:
            print("-->> Test case for \"Help\" is unsuccessful!")
        if Canada411Home.dncl_is_success:
            print("-->> Test case for \"DNCL\" is successful!")
        else:
            print("-->> Test case for \"DNCL\" is unsuccessful!")
        if Canada411Home.request_res_dir_is_success:
            print("-->> Test case for \"Request a Residential Directory\" is successful!")
        else:
            print("-->> Test case for \"Request a Residential Directory\" is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_quick_links(My.c411_qa_web_link)
