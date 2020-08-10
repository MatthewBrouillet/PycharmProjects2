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
    contact_us_is_success = False
    careers_is_success = False
    privacy_policy_is_success = False
    terms_conditions_is_success = False

    def about_us_quick_links(self, link):
        """
        >> This function verifies if the "About us" quick links are clickable and functional
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
                driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[1]/li[" + str(count + 1) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                # print(str(driver.current_url))
                if driver.current_url == link + "about/contact.html":
                    Canada411Home.contact_us_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                # print(str(driver.current_url))
                if driver.current_url == "https://jobs.ypg.com/":
                    Canada411Home.careers_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                # print(str(driver.current_url))
                if driver.current_url == My.corporate_web_link + "legal-notice/privacy-statement/":
                    Canada411Home.privacy_policy_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                # print(str(driver.current_url))
                if driver.current_url == My.corporate_web_link + "legal-notice/terms-of-use-agreement/":
                    Canada411Home.terms_conditions_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_about_us_quick_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.about_us_quick_links(link)
        if Canada411Home.contact_us_is_success:
            print("-->> Test case for \"Contact us\" is successful!")
        else:
            print("-->> Test case for \"Contact us\" is unsuccessful!")
        if Canada411Home.careers_is_success:
            print("-->> Test case for \"Careers\" is successful!")
        else:
            print("-->> Test case for \"Careers\" is unsuccessful!")
        if Canada411Home.privacy_policy_is_success:
            print("-->> Test case for \"Privacy policy\" is successful!")
        else:
            print("-->> Test case for \"Privacy policy\" is unsuccessful!")
        if Canada411Home.terms_conditions_is_success:
            print("-->> Test case for \"Terms and conditions\" is successful!")
        else:
            print("-->> Test case for \"Terms and conditions\" is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_about_us_quick_links(My.c411_qa_web_link)
