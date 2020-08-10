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
                if count == 1:
                    if heading_link.text == 'Restaurants':
                        YPPopularHeadings.restaurants_is_success = True
                    else:
                        pass
                if count == 2:
                    if link == My.yp_web_link + "/search/si/1/restaurants/Montreal+QC":
                        if heading_link.text == 'Dentists':
                            YPPopularHeadings.dentists_is_success = True
                        else:
                            pass
                    else:
                        if heading_link.text == 'Dentistes':
                            YPPopularHeadings.dentists_is_success = True
                        else:
                            pass
                if count == 3:
                    if link == My.yp_web_link + "/search/si/1/restaurants/Montreal+QC":
                        if heading_link.text == 'Medical Clinics':
                            YPPopularHeadings.medical_clinics_is_success = True
                        else:
                            pass
                    else:
                        if heading_link.text == 'Cliniques Médicales':
                            YPPopularHeadings.medical_clinics_is_success = True
                        else:
                            pass
                if count == 4:
                    if link == My.yp_web_link + "/search/si/1/restaurants/Montreal+QC":
                        if heading_link.text == 'Car Repair':
                           YPPopularHeadings.car_repair_is_success = True
                        else:
                            pass
                    else:
                        if heading_link.text == 'Réparation De Voitures':
                            YPPopularHeadings.car_repair_is_success = True
                        else:
                            pass
                if count == 5:
                    if link == My.yp_web_link + "/search/si/1/restaurants/Montreal+QC":
                        if heading_link.text == 'Grocery Stores':
                            YPPopularHeadings.grocery_stores_is_success = True
                        else:
                            pass
                    else:
                        if heading_link.text == 'Épiceries':
                            YPPopularHeadings.grocery_stores_is_success = True
                        else:
                            pass
            else:
                return

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
