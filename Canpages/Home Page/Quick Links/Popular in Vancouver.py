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
    restaurants_is_success = False
    beauty_salons_is_success = False
    plumbers_is_success = False
    chiropractors_is_success = False
    hotels_is_success = False
    florists_is_success = False

    def popular_vancouver(self, link):
        """
        >> This function verifies if the Popular in Vancouver links are clickable and functional.
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
                driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[5]/ul/li[' + str(count) + ']/a')
            if quick_link:
                quick_link.click()
                pass
            else:
                pass

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + 'business/BC/vancouver/restaurants/961-720200.html':
                    CanPagesQuickLinks.restaurants_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + 'business/BC/vancouver/beauty-salons/961-072400.html':
                    CanPagesQuickLinks.beauty_salons_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + 'business/BC/vancouver/plumbing-contractors/961-667800.html':
                    CanPagesQuickLinks.plumbers_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + 'business/BC/vancouver/chiropractors-dc/961-155400.html':
                    CanPagesQuickLinks.chiropractors_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + \
                        'business/BC/vancouver/hotels-motels-and-other-accommodations/961-419600.html':
                    CanPagesQuickLinks.hotels_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + 'business/BC/vancouver/florists-retail/961-335600.html':
                    CanPagesQuickLinks.florists_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_popular_vancouver(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.popular_vancouver(link)
        if CanPagesQuickLinks.restaurants_is_success:
            print("--> Test case for \"Restaurants\" is successful.")
        else:
            print("--> Test case for \"Restaurants\" is unsuccessful.")
        if CanPagesQuickLinks.beauty_salons_is_success:
            print("--> Test case for \"Beauty Salons\" is successful.")
        else:
            print("--> Test case for \"Beauty Salons\" is unsuccessful.")
        if CanPagesQuickLinks.plumbers_is_success:
            print("--> Test case for \"Plumbers\" is successful.")
        else:
            print("--> Test case for \"Plumbers\" is unsuccessful.")
        if CanPagesQuickLinks.chiropractors_is_success:
            print("--> Test case for \"Chiropractors\" is successful.")
        else:
            print("--> Test case for \"Chiropractors\" is unsuccessful.")
        if CanPagesQuickLinks.hotels_is_success:
            print("--> Test case for \"Hotels\" is successful.")
        else:
            print("--> Test case for \"Hotels\" is unsuccessful.")
        if CanPagesQuickLinks.florists_is_success:
            print("--> Test case for \"Florists\" is successful.")
        else:
            print("--> Test case for \"Florists\" is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesQuickLinks(driver)
test.testing_popular_vancouver(My.canpages_web_link)
