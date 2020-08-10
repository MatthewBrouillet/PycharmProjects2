import sys
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
    advertise_with_us_is_success = False
    add_a_free_listing_is_success = False
    fraud_prevention_is_success = False

    def quick_links_advertisers(self, link):
        """
        >> This function verifies if the "Advertisers" quick links are clickable and functional
        """
        count = 1
        while count < 4:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH,
                "//*[@id='ypgFooter']/div[2]/div[2]/div[2]/div[2]/ul/li[" + str(count) + "]/a")
            # print('Count: ' + str(count))

            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                if driver.current_url == "https://business.yellowpages.ca/home/#/":
                    YPQuickLinks.advertise_with_us_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                window_after = driver.window_handles[2]
                driver.switch_to.window(window_after)
                if driver.current_url == \
                        "https://business.yellowpages.ca/onboarding/#/" \
                        "free-listing-yellow-pages?utm_source=ypca&utm_medium=link&utm_campaign=footer":
                    YPQuickLinks.add_a_free_listing_is_success = True
                    pass
                else:
                    pass
            else:
                window_after = driver.window_handles[3]
                driver.switch_to.window(window_after)
                if link == My.yp_web_link:
                    if driver.current_url == "https://businesscentre.yp.ca/-/fraud-preventi-1":
                        YPQuickLinks.fraud_prevention_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == "https://businesscentre.yp.ca/-/fraud-preventi-1":
                        YPQuickLinks.fraud_prevention_is_success = True
                        pass
                    else:
                        pass
            count += 1
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)

    def testing_quick_links_advertisers(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.quick_links_advertisers(link)
        if YPQuickLinks.advertise_with_us_is_success:
            print("-->> Test case for \"Advertise with Us\" is successful!")
        else:
            print("-->> Test case for \"Advertise with Us\" is unsuccessful!")
        if YPQuickLinks.add_a_free_listing_is_success:
            print("-->> Test case for \"Add a Free Listing\" is successful!")
        else:
            print("-->> Test case for \"Add a Free Listing\" is unsuccessful!")
        if YPQuickLinks.fraud_prevention_is_success:
            print("-->> Test case for \"Fraud Prevention\" is successful!")
        else:
            print("-->> Test case for \"Fraud Prevention\" is unsuccessful!")


test = YPQuickLinks(driver)
test.testing_quick_links_advertisers(My.yp_web_link)
print('----------')
test.testing_quick_links_advertisers(My.pj_web_link)
driver.quit()
sys.exit()
