import sys
import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPQuickLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    contact_yp_is_success = False
    careers_is_success = False
    investors_is_success = False
    corporate_is_success = False
    private_statement_is_success = False
    terms_of_use_is_success = False
    help_is_success = False

    def quick_links_about_us(self, link):
        """
        >> This function verifies if the "About us" quick links are clickable and functional
        """
        count = 1
        while count < 11:
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[3]/div[2]/ul/li[" + str(count) + "]/a")
            print('Count: ' + str(count))

            if quick_link:
                quick_link.click()
            else:
                pass

            if count == 1:
                if driver.current_url == My.yp_web_link + "/contactus":
                    YPQuickLinks.contact_yp_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                if driver.current_url == "https://jobs-emplois.yp.ca":
                    YPQuickLinks.careers_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                window_after = driver.window_handles[2]
                driver.switch_to.window(window_after)
                if driver.current_url == "https://corporate.yp.ca/en/investors/overview/":
                    YPQuickLinks.investors_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                window_after = driver.window_handles[3]
                driver.switch_to.window(window_after)
                if driver.current_url == "https://corporate.yp.ca/en/":
                    YPQuickLinks.corporate_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                window_after = driver.window_handles[4]
                driver.switch_to.window(window_after)
                if driver.current_url == "https://corporate.yp.ca/en/legal-notice/privacy-statement/":
                    YPQuickLinks.private_statement_is_success = True
                    pass
                else:
                    pass
            elif count == 6:
                window_after = driver.window_handles[5]
                driver.switch_to.window(window_after)
                if driver.current_url == "https://corporate.yp.ca/en/legal-notice/terms-of-use-agreement/":
                    YPQuickLinks.terms_of_use_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == My.yp_web_link + "/help.html":
                    YPQuickLinks.help_is_success = True
                    pass
                else:
                    pass

            if count == (2 or 3 or 4 or 5 or 6):
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
            else:
                driver.back()
            count += 1

    def testing_quick_links_about_us(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.quick_links_about_us(link)
        if YPQuickLinks.contact_yp_is_success:
            print("-->> Test case for \"Contact us\" is successful!")
        else:
            print("-->> Test case for \"Contact us\" is unsuccessful!")
        if YPQuickLinks.careers_is_success:
            print("-->> Test case for \"Careers\" is successful!")
        else:
            print("-->> Test case for \"Careers\" is unsuccessful!")
        if YPQuickLinks.investors_is_success:
            print("-->> Test case for \"Investors\" is successful!")
        else:
            print("-->> Test case for \"Investors\" is unsuccessful!")
        if YPQuickLinks.corporate_is_success:
            print("-->> Test case for \"Corporate\" is successful!")
        else:
            print("-->> Test case for \"Corporate\" is unsuccessful!")
        if YPQuickLinks.private_statement_is_success:
            print("-->> Test case for \"Private Statement\" is successful!")
        else:
            print("-->> Test case for \"Private Statement\" is unsuccessful!")
        if YPQuickLinks.terms_of_use_is_success:
            print("-->> Test case for \"Terms of use\" is successful!")
        else:
            print("-->> Test case for \"Terms of use\" is unsuccessful!")
        if YPQuickLinks.help_is_success:
            print("-->> Test case for \"Help\" is successful!")
        else:
            print("-->> Test case for \"Help\" is unsuccessful!")
        time.sleep(5)
        driver.quit()
        sys.exit()


"""
>> MAIN
"""
test = YPQuickLinks(driver)
test.testing_quick_links_about_us(My.yp_web_link)
