import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class CanPagesLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    banks_is_success = False
    bars_is_success = False
    clinics_is_success = False
    nail_salons_is_success = False
    dentists_is_success = False
    florists_is_success = False
    jobs_is_success = False
    pharmacies_is_success = False
    pizza_is_success = False
    restaurants_is_success = False

    def quick_links(self, link):
        """
        >> This function verifies if the Quick Links are clickable and functional.
        """

        count = 1
        while count < 11:

            # Locating the quick link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='top-categories']/li[" + str(count) + "]/a")
            if quick_link:
                quick_link.click()
                pass
            else:
                pass

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Banks":
                    CanPagesLinks.banks_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Bars":
                    CanPagesLinks.bars_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Clinics":
                    CanPagesLinks.clinics_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Nail+Salons":
                    CanPagesLinks.nail_salons_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Dentists":
                    CanPagesLinks.dentists_is_success = True
                    pass
                else:
                    pass
            elif count == 6:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Florists":
                    CanPagesLinks.florists_is_success = True
                    pass
                else:
                    pass
            elif count == 7:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Jobs":
                    CanPagesLinks.jobs_is_success = True
                    pass
                else:
                    pass
            elif count == 8:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Pharmacies":
                    CanPagesLinks.pharmacies_is_success = True
                    pass
                else:
                    pass
            elif count == 9:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Pizza":
                    CanPagesLinks.pizza_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + "list.jsp?ct=M5H+3B7&na=Restaurants":
                    CanPagesLinks.restaurants_is_success = True
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
        if CanPagesLinks.banks_is_success:
            print("--> Test case for \"Banks\" is successful.")
        else:
            print("--> Test case for \"Banks\" is unsuccessful.")
        if CanPagesLinks.bars_is_success:
            print("--> Test case for \"Bars\" is successful.")
        else:
            print("--> Test case for \"Bars\" is unsuccessful.")
        if CanPagesLinks.clinics_is_success:
            print("--> Test case for \"Clinics\" is successful.")
        else:
            print("--> Test case for \"Clinics\" is unsuccessful.")
        if CanPagesLinks.nail_salons_is_success:
            print("--> Test case for \"Nail Salons\" is successful.")
        else:
            print("--> Test case for \"Nail Salons\" is unsuccessful.")
        if CanPagesLinks.dentists_is_success:
            print("--> Test case for \"Dentists\" is successful.")
        else:
            print("--> Test case for \"Dentists\" is unsuccessful.")
        if CanPagesLinks.florists_is_success:
            print("--> Test case for \"Florists\" is successful.")
        else:
            print("--> Test case for \"Florists\" is unsuccessful.")
        if CanPagesLinks.jobs_is_success:
            print("--> Test case for \"Jobs\" is successful.")
        else:
            print("--> Test case for \"Jobs\" is unsuccessful.")
        if CanPagesLinks.pharmacies_is_success:
            print("--> Test case for \"Pharmacies\" is successful.")
        else:
            print("--> Test case for \"Pharmacies\" is unsuccessful.")
        if CanPagesLinks.pizza_is_success:
            print("--> Test case for \"Pizza\" is successful.")
        else:
            print("--> Test case for \"Pizza\" is unsuccessful.")
        if CanPagesLinks.restaurants_is_success:
            print("--> Test case for \"Restaurants\" is successful.")
        else:
            print("--> Test case for \"Restaurants\" is unsuccessful.")


test = CanPagesLinks(driver)
test.testing_quick_links(My.canpages_web_link)
driver.quit()
sys.exit()
