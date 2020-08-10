import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPPopularHeadings:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    restaurants_is_success = False
    dentists_is_success = False
    medical_clinics_is_success = False
    car_repair_is_success = False
    grocery_stores_is_success = False

    def popular_headings(self, link):
        """
        >> This function validates the headings below the search bar on the header.
        """
        count = 1
        while count < 6:

            # Locating the heading link depending on the count value
            heading_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/ul/li[" + str(count) + "]/a")
            if heading_link:
                heading_link.click()
            else:
                return

            if count == 1:
                if link[0:26] == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + '/search/si/1/Restaurants/Montreal+QC':
                        YPPopularHeadings.restaurants_is_success = True
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + '/search/si/1/Restaurants/Montreal+QC':
                        YPPopularHeadings.restaurants_is_success = True
                    else:
                        pass
            if count == 2:
                if link[0:26] == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + '/search/si/1/Dentists/Montreal+QC':
                        YPPopularHeadings.dentists_is_success = True
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + '/search/si/1/Dentistes/Montreal+QC':
                        YPPopularHeadings.dentists_is_success = True
                    else:
                        pass
            if count == 3:
                if link[0:26] == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + '/search/si/1/Medical+Clinics/Montreal+QC':
                        YPPopularHeadings.medical_clinics_is_success = True
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + '/search/si/1/Cliniques+medicales/Montreal+QC':
                        YPPopularHeadings.medical_clinics_is_success = True
                    else:
                        pass
            if count == 4:
                if link[0:26] == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + '/search/si/1/Car+Repair/Montreal+QC':
                        YPPopularHeadings.car_repair_is_success = True
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + '/search/si/1/Reparation+de+voitures/Montreal+QC':
                        YPPopularHeadings.car_repair_is_success = True
                    else:
                        pass
            if count == 5:
                if link[0:26] == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + '/search/si/1/Grocery+Stores/Montreal+QC':
                        YPPopularHeadings.grocery_stores_is_success = True
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + '/search/si/1/Epiceries/Montreal+QC':
                        YPPopularHeadings.grocery_stores_is_success = True
                    else:
                        pass

            count += 1

    def testing_popular_headings(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.popular_headings(link)
        if YPPopularHeadings.restaurants_is_success:
            print("--> Test case for \"Restaurants\" is successful.")
        else:
            print("--> Test case for \"Restaurants\" is unsuccessful.")
        if YPPopularHeadings.dentists_is_success:
            print("--> Test case for \"Dentists\" is successful.")
        else:
            print("--> Test case for \"Dentists\" is unsuccessful.")
        if YPPopularHeadings.medical_clinics_is_success:
            print("--> Test case for \"Medical Clinics\" is successful.")
        else:
            print("--> Test case for \"Medical Clinics\" is unsuccessful.")
        if YPPopularHeadings.car_repair_is_success:
            print("--> Test case for \"Car Repair\" is successful.")
        else:
            print("--> Test case for \"Car Repair\" is unsuccessful.")
        if YPPopularHeadings.grocery_stores_is_success:
            print("--> Test case for \"Grocery Stores\" is successful.")
        else:
            print("--> Test case for \"Grocery Stores\" is unsuccessful.")


test = YPPopularHeadings(driver)
test.testing_popular_headings(My.yp_web_link + "/search/si/1/restaurants/Montreal+QC")
print('----------')
test.testing_popular_headings(My.pj_web_link + "/search/si/1/restaurants/Montreal+QC")
driver.quit()
sys.exit()
