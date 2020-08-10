import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class CanPagesQuickLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    movers_is_success = False
    electricians_is_success = False
    dentists_is_success = False
    painters_is_success = False
    plumbers_is_success = False
    roofers_is_success = False

    def popular_calgary(self, link):
        """
        >> This function verifies if the Popular in Edmonton links are clickable and functional.
        """
        # Locating the Quick Links toggle
        quick_links_toggle = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="footer"]/div[1]/div[1]/a[1]')
        if quick_links_toggle:
            quick_links_toggle.click()
            pass
        else:
            return

        count = 1
        while count < 7:
            # Locating the Links container
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[4]/ul/li[' + str(count) + ']/a')
            if quick_link:
                quick_link.click()
                pass
            else:
                pass

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + 'business/AB/edmonton/movers/183-544400.html':
                    CanPagesQuickLinks.movers_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + 'business/AB/edmonton/electrical-contractors/183-275200.html':
                    CanPagesQuickLinks.electricians_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + 'business/AB/edmonton/dentists/183-239800.html':
                    CanPagesQuickLinks.dentists_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + 'business/AB/edmonton/painters-and-painting-contractors/183-587400.html':
                    CanPagesQuickLinks.painters_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + 'business/AB/edmonton/plumbing-contractors/183-667800.html':
                    CanPagesQuickLinks.plumbers_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + 'business/AB/edmonton/roofing-contractors/183-727400.html':
                    CanPagesQuickLinks.roofers_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_popular_calgary(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.popular_calgary(link)
        if CanPagesQuickLinks.movers_is_success:
            print("--> Test case for \"Movers\" is successful.")
        else:
            print("--> Test case for \"Movers\" is unsuccessful.")
        if CanPagesQuickLinks.electricians_is_success:
            print("--> Test case for \"Electricians\" is successful.")
        else:
            print("--> Test case for \"Electricians\" is unsuccessful.")
        if CanPagesQuickLinks.dentists_is_success:
            print("--> Test case for \"Dentists\" is successful.")
        else:
            print("--> Test case for \"Dentists\" is unsuccessful.")
        if CanPagesQuickLinks.painters_is_success:
            print("--> Test case for \"Painters\" is successful.")
        else:
            print("--> Test case for \"Painters\" is unsuccessful.")
        if CanPagesQuickLinks.plumbers_is_success:
            print("--> Test case for \"Plumbers\" is successful.")
        else:
            print("--> Test case for \"Plumbers\" is unsuccessful.")
        if CanPagesQuickLinks.roofers_is_success:
            print("--> Test case for \"Roofers\" is successful.")
        else:
            print("--> Test case for \"Roofers\" is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesQuickLinks(driver)
test.testing_popular_calgary(My.canpages_web_link)
