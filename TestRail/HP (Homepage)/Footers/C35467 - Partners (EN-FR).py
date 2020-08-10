import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPPartners:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    ca_411_is_success = False
    canpages_is_success = False

    def partners(self, link):
        """
        >> This function verifies if the "Partners" quick links are clickable and functional
        """
        count = 1
        while count < 3:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH,
                "//*[@id='ypgFooter']/div[2]/div[2]/div[6]/div[2]/ul/li[" + str(count) + "]/a")

            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                if link == My.yp_web_link:
                    if driver.current_url == "https://www.canada411.ca/":
                        YPPartners.ca_411_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == "https://www.fr.canada411.ca/":
                        YPPartners.ca_411_is_success = True
                        pass
                    else:
                        pass
            else:
                if link == My.yp_web_link:
                    if driver.current_url == "https://www.canpages.ca/":
                        YPPartners.canpages_is_success = True
                        return
                    else:
                        return
                else:
                    if driver.current_url == "https://www.canpages.ca/fr/":
                        YPPartners.canpages_is_success = True
                        return
                    else:
                        return
            count += 1
            driver.back()

    def testing_partners(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.partners(link)
        if YPPartners.ca_411_is_success:
            print("-->> Test case for \"Canada411.ca\" is successful!")
        else:
            print("-->> Test case for \"Canada411.ca\" is unsuccessful!")
        if YPPartners.canpages_is_success:
            print("-->> Test case for \"Canpages.ca\" is successful!")
        else:
            print("-->> Test case for \"Canpages.ca\" is unsuccessful!")


test = YPPartners(driver)
test.testing_partners(My.yp_web_link)
print('----------')
test.testing_partners(My.pj_web_link)
driver.quit()
sys.exit()
