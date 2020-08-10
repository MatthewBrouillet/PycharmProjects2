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
    pizza_is_success = False
    bars_is_success = False
    beauty_salons_is_success = False
    hotels_is_success = False
    hospitals_is_success = False
    medical_clinics_is_success = False
    doctors_is_success = False
    dentists_is_success = False
    lawyers_is_success = False

    def quick_links_popular_searches(self, link):
        """
        >> This function verifies if the "Popular Searches" quick links are clickable and functional
        """
        count = 1
        while count < 11:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH,
                "//*[@id='ypgFooter']/div[2]/div[2]/div[1]/div[2]/ul/li[" + str(count) + "]/a")
            # print('Count: ' + str(count))

            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                if driver.current_url == link + "/business/01125710.html":
                    YPQuickLinks.restaurants_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + "/business/01012401.html":
                    YPQuickLinks.pizza_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + "/business/00126870.html":
                    YPQuickLinks.bars_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + "/business/00135600.html":
                    YPQuickLinks.beauty_salons_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + "/business/00682205.html":
                    YPQuickLinks.hotels_is_success = True
                    pass
                else:
                    pass
            elif count == 6:
                if driver.current_url == link + "/business/00681600.html":
                    YPQuickLinks.hospitals_is_success = True
                    pass
                else:
                    pass
            elif count == 7:
                if driver.current_url == link + "/business/00304200.html":
                    YPQuickLinks.medical_clinics_is_success = True
                    pass
                else:
                    pass
            elif count == 8:
                if driver.current_url == link + "/business/90010010.html":
                    YPQuickLinks.doctors_is_success = True
                    pass
                else:
                    pass
            elif count == 9:
                if driver.current_url == link + "/business/00414600.html":
                    YPQuickLinks.dentists_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + "/business/00761600.html":
                    YPQuickLinks.lawyers_is_success = True
                    pass
                else:
                    pass
            count += 1
            driver.back()

    def testing_quick_links_popular_searches(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.quick_links_popular_searches(link)
        if YPQuickLinks.restaurants_is_success:
            print("-->> Test case for \"Restaurants\" is successful!")
        else:
            print("-->> Test case for \"Restaurants\" is unsuccessful!")
        if YPQuickLinks.pizza_is_success:
            print("-->> Test case for \"Pizza\" is successful!")
        else:
            print("-->> Test case for \"Pizza\" is unsuccessful!")
        if YPQuickLinks.bars_is_success:
            print("-->> Test case for \"Bars\" is successful!")
        else:
            print("-->> Test case for \"Bars\" is unsuccessful!")
        if YPQuickLinks.beauty_salons_is_success:
            print("-->> Test case for \"Beauty Salons\" is successful!")
        else:
            print("-->> Test case for \"Beauty Salons\" is unsuccessful!")
        if YPQuickLinks.hotels_is_success:
            print("-->> Test case for \"Hotels\" is successful!")
        else:
            print("-->> Test case for \"Hotels\" is unsuccessful!")
        if YPQuickLinks.hospitals_is_success:
            print("-->> Test case for \"Hospitals\" is successful!")
        else:
            print("-->> Test case for \"Hospitals\" is unsuccessful!")
        if YPQuickLinks.medical_clinics_is_success:
            print("-->> Test case for \"Medical Clinics\" is successful!")
        else:
            print("-->> Test case for \"Medical Clinics\" is unsuccessful!")
        if YPQuickLinks.doctors_is_success:
            print("-->> Test case for \"Doctors\" is successful!")
        else:
            print("-->> Test case for \"Doctors\" is unsuccessful!")
        if YPQuickLinks.dentists_is_success:
            print("-->> Test case for \"Dentists\" is successful!")
        else:
            print("-->> Test case for \"Dentists\" is unsuccessful!")
        if YPQuickLinks.lawyers_is_success:
            print("-->> Test case for \"Lawyers\" is successful!")
        else:
            print("-->> Test case for \"Lawyers\" is unsuccessful!")


test = YPQuickLinks(driver)
test.testing_quick_links_popular_searches(My.yp_web_link)
print('----------')
test.testing_quick_links_popular_searches(My.pj_web_link)
driver.quit()
sys.exit()
