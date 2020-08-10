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
    canadaplus_is_success = False
    employment_news_is_success = False
    hometrader_is_success = False
    hospital_news_is_success = False
    mediative_is_success = False
    restaurantica_is_success = False
    ypca_is_success = False

    def our_partners_quick_links(self, link):
        """
        >> This function verifies if the "Our partners" quick links are clickable and functional
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
        if footer_container:
            pass
        else:
            return

        count = 1
        while count < 4:
            # print(str(count))
            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[4]/li[" + str(count + 1) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                # print(str(driver.current_url))
                if driver.current_url == "https://www.canadaplus.ca/":
                    Canada411Home.canadaplus_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                # print(str(driver.current_url))
                if driver.current_url == "https://www.employmentnews.com/":
                    Canada411Home.employment_news_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                # print(str(driver.current_url))
                if driver.current_url == "https://www.canpages.ca/":
                    Canada411Home.hometrader_is_success = True
                    pass
                else:
                    pass
            count += 1
            driver.back()

        while count < 6:
            # print(str(count))
            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[5]/li[" + str(count - 2) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            if count == 4:
                # print(str(driver.current_url))
                if driver.current_url == "https://hospitalnews.com/":
                    Canada411Home.hospital_news_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                # print(str(driver.current_url))
                if driver.current_url == "https://mediative.com/":
                    Canada411Home.mediative_is_success = True
                    pass
                else:
                    pass
            count += 1
            driver.back()

        while count < 8:
            # print(str(count))
            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[6]/li[" + str(count - 4) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            if count == 6:
                # print(str(driver.current_url))
                if driver.current_url == "https://www.restaurantica.com/":
                    Canada411Home.restaurantica_is_success = True
                    pass
                else:
                    pass
            else:
                # print(str(driver.current_url))
                if driver.current_url == My.yp_web_link + "/":
                    Canada411Home.ypca_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_our_partners_quick_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.our_partners_quick_links(link)
        if Canada411Home.canadaplus_is_success:
            print("-->> Test case for \"CanadaPlus.ca\" is successful!")
        else:
            print("-->> Test case for \"CanadaPlus.ca\" is unsuccessful!")
        if Canada411Home.employment_news_is_success:
            print("-->> Test case for \"Employment News\" is successful!")
        else:
            print("-->> Test case for \"Employment News\" is unsuccessful!")
        if Canada411Home.hometrader_is_success:
            print("-->> Test case for \"HomeTrader.ca\" is successful!")
        else:
            print("-->> Test case for \"HomeTrader.ca\" is unsuccessful!")
        if Canada411Home.hospital_news_is_success:
            print("-->> Test case for \"Hospital News\" is successful!")
        else:
            print("-->> Test case for \"Hospital News\" is unsuccessful!")
        if Canada411Home.mediative_is_success:
            print("-->> Test case for \"Mediative.com\" is successful!")
        else:
            print("-->> Test case for \"Mediative.com\" is unsuccessful!")
        if Canada411Home.restaurantica_is_success:
            print("-->> Test case for \"Restaurantica.com\" is successful!")
        else:
            print("-->> Test case for \"Restaurantica.com\" is unsuccessful!")
        if Canada411Home.ypca_is_success:
            print("-->> Test case for \"YP.ca\" is successful!")
        else:
            print("-->> Test case for \"YP.ca\" is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_our_partners_quick_links(My.c411_qa_web_link)
