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
    dentists_is_success = False
    lawyers_is_success = False
    restaurants_is_success = False
    roofers_is_success = False
    car_repairs_is_success = False
    electricians_is_success = False

    def popular_calgary(self, link):
        """
        >> This function verifies if the Popular in Calgary links are clickable and functional.
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
                driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[3]/ul/li[' + str(count) + ']/a')
            if quick_link:
                quick_link.click()
                pass
            else:
                pass

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + 'business/AB/calgary/dentists/91-239800.html':
                    CanPagesQuickLinks.dentists_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + 'business/AB/calgary/lawyers/91-464400.html':
                    CanPagesQuickLinks.lawyers_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + 'business/AB/calgary/restaurants/91-720200.html':
                    CanPagesQuickLinks.restaurants_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + 'business/AB/calgary/roofing-contractors/91-727400.html':
                    CanPagesQuickLinks.roofers_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + 'business/AB/calgary/automobile-repairing-and-service/91-052200.html':
                    CanPagesQuickLinks.car_repairs_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + 'business/AB/calgary/electrical-contractors/91-275200.html':
                    CanPagesQuickLinks.electricians_is_success = True
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
        if CanPagesQuickLinks.dentists_is_success:
            print("--> Test case for \"Dentists\" is successful.")
        else:
            print("--> Test case for \"Dentists\" is unsuccessful.")
        if CanPagesQuickLinks.lawyers_is_success:
            print("--> Test case for \"Lawyers\" is successful.")
        else:
            print("--> Test case for \"Lawyers\" is unsuccessful.")
        if CanPagesQuickLinks.restaurants_is_success:
            print("--> Test case for \"Restaurants\" is successful.")
        else:
            print("--> Test case for \"Restaurants\" is unsuccessful.")
        if CanPagesQuickLinks.roofers_is_success:
            print("--> Test case for \"Roofers\" is successful.")
        else:
            print("--> Test case for \"Roofers\" is unsuccessful.")
        if CanPagesQuickLinks.car_repairs_is_success:
            print("--> Test case for \"Car Repairs\" is successful.")
        else:
            print("--> Test case for \"Car Repairs\" is unsuccessful.")
        if CanPagesQuickLinks.electricians_is_success:
            print("--> Test case for \"Electricians\" is successful.")
        else:
            print("--> Test case for \"Electricians\" is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesQuickLinks(driver)
test.testing_popular_calgary(My.canpages_web_link)
