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
    restaurants_is_success = False
    dentist_is_success = False
    medical_clinics_is_success = False
    car_repair_is_success = False
    grocery_is_success = False

    def quick_links(self, link):
        """
        >> This function verifies if the quick link are clickable
        >> and leads to the right URL
        """
        count = 1
        while count < 6:

            # Locating the toggle
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='ypgBody']/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[" + str(count) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                return

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + "/search/si/1/Restaurants/Montreal+QC":
                    YPQuickLinks.restaurants_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if link == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + "/search/si/1/Dentists/Montreal+QC":
                        YPQuickLinks.dentist_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == My.yp_web_link + "/search/si/1/Dentistes/Montreal+QC":
                        YPQuickLinks.dentist_is_success = True
                        pass
                    else:
                        pass
            elif count == 3:
                if link == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + "/search/si/1/Medical+Clinics/Montreal+QC":
                        YPQuickLinks.medical_clinics_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + "/search/si/1/Cliniques+medicales/Montreal+QC":
                        YPQuickLinks.medical_clinics_is_success = True
                        pass
                    else:
                        pass
            elif count == 4:
                if link == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + "/search/si/1/Car+Repair/Montreal+QC":
                        YPQuickLinks.car_repair_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == My.pj_web_link + "/search/si/1/Reparation+de+voitures/Montreal+QC":
                        YPQuickLinks.car_repair_is_success = True
                        pass
                    else:
                        pass
            else:
                if link == My.yp_web_link:
                    if driver.current_url == My.yp_web_link + "/search/si/1/Grocery+Stores/Montreal+QC":
                        YPQuickLinks.grocery_is_success = True
                        return
                    else:
                        return
                else:
                    if driver.current_url == My.pj_web_link + "/search/si/1/Epiceries/Montreal+QC":
                        YPQuickLinks.grocery_is_success = True
                        return
                    else:
                        return
            count += 1
            driver.back()

    def testing_quick_links(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.quick_links(link)
        if YPQuickLinks.restaurants_is_success:
            print("--> Test case is for \"Restaurants\" successful.")
        else:
            print("--> Test case is for \"Restaurants\" unsuccessful.")
        if YPQuickLinks.dentist_is_success:
            print("--> Test case is for \"Dentists\" successful.")
        else:
            print("--> Test case is for \"Dentists\" unsuccessful.")
        if YPQuickLinks.medical_clinics_is_success:
            print("--> Test case is for \"Medical Clinics\" successful.")
        else:
            print("--> Test case is for \"Medical Clinics\" unsuccessful.")
        if YPQuickLinks.car_repair_is_success:
            print("--> Test case is for \"Car Repair\" successful.")
        else:
            print("--> Test case is for \"Car Repair\" unsuccessful.")
        if YPQuickLinks.grocery_is_success:
            print("--> Test case is for \"Grocery Stores\" successful.")
        else:
            print("--> Test case is for \"Grocery Stores\" unsuccessful.")


test = YPQuickLinks(driver)
test.testing_quick_links(My.yp_web_link)
print('----------')
test.testing_quick_links(My.pj_web_link)
driver.quit()
sys.exit()
