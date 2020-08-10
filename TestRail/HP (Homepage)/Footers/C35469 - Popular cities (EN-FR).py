import sys
import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPPopularCities:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    calgary_is_success = False
    edmonton_is_success = False
    gatineau_is_success = False
    hamilton_is_success = False
    toronto_is_success = False
    winnipeg_is_success = False
    vancouver_is_success = False
    montreal_is_success = False
    ottawa_is_success = False
    quebec_is_success = False

    def popular_cities(self, link):
        """
        >> This function verifies if the "Popular Cities" quick links are clickable and functional
        """
        count = 1
        while count < 11:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH,
                "//*[@id='ypgFooter']/div[2]/div[2]/div[1]/div[4]/ul/li[" + str(count) + "]/a")
            # print('Count: ' + str(count))

            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                if driver.current_url == link + "/locations/Alberta/Calgary":
                    YPPopularCities.calgary_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + "/locations/Alberta/Edmonton":
                    YPPopularCities.edmonton_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + "/locations/Quebec/Gatineau":
                    YPPopularCities.gatineau_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + "/locations/Ontario/Hamilton":
                    YPPopularCities.hamilton_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + "/locations/Ontario/Toronto":
                    YPPopularCities.toronto_is_success = True
                    pass
                else:
                    pass
            elif count == 6:
                if driver.current_url == link + "/locations/Manitoba/Winnipeg":
                    YPPopularCities.winnipeg_is_success = True
                    pass
                else:
                    pass
            elif count == 7:
                if driver.current_url == link + "/locations/British-Columbia/Vancouver":
                    YPPopularCities.vancouver_is_success = True
                    pass
                else:
                    pass
            elif count == 8:
                if driver.current_url == link + "/locations/Quebec/Montreal":
                    YPPopularCities.montreal_is_success = True
                    pass
                else:
                    pass
            elif count == 9:
                if driver.current_url == link + "/locations/Ontario/Ottawa":
                    YPPopularCities.ottawa_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + "/locations/Quebec/Quebec":
                    YPPopularCities.quebec_is_success = True
                    return
                else:
                    pass
            count += 1
            driver.back()

    def testing_popular_cities(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.popular_cities(link)
        if YPPopularCities.calgary_is_success:
            print("-->> Test case for \"Calgary\" is successful!")
        else:
            print("-->> Test case for \"Calgary\" is unsuccessful!")
        if YPPopularCities.edmonton_is_success:
            print("-->> Test case for \"Edmonton\" is successful!")
        else:
            print("-->> Test case for \"Edmonton\" is unsuccessful!")
        if YPPopularCities.gatineau_is_success:
            print("-->> Test case for \"Gatineau\" is successful!")
        else:
            print("-->> Test case for \"Gatineau\" is unsuccessful!")
        if YPPopularCities.hamilton_is_success:
            print("-->> Test case for \"Hamilton\" is successful!")
        else:
            print("-->> Test case for \"Hamilton\" is unsuccessful!")
        if YPPopularCities.toronto_is_success:
            print("-->> Test case for \"Toronto\" is successful!")
        else:
            print("-->> Test case for \"Toronto\" is unsuccessful!")
        if YPPopularCities.winnipeg_is_success:
            print("-->> Test case for \"Winnipeg\" is successful!")
        else:
            print("-->> Test case for \"Winnipeg\" is unsuccessful!")
        if YPPopularCities.vancouver_is_success:
            print("-->> Test case for \"Vancouver\" is successful!")
        else:
            print("-->> Test case for \"Vancouver\" is unsuccessful!")
        if YPPopularCities.montreal_is_success:
            print("-->> Test case for \"Montreal\" is successful!")
        else:
            print("-->> Test case for \"Montreal\" is unsuccessful!")
        if YPPopularCities.ottawa_is_success:
            print("-->> Test case for \"Ottawa\" is successful!")
        else:
            print("-->> Test case for \"Ottawa\" is unsuccessful!")
        if YPPopularCities.quebec_is_success:
            print("-->> Test case for \"Quebec\" is successful!")
        else:
            print("-->> Test case for \"Quebec\" is unsuccessful!")


test = YPPopularCities(driver)
test.testing_popular_cities(My.yp_web_link)
print('----------')
test.testing_popular_cities(My.pj_web_link)
driver.quit()
sys.exit()
