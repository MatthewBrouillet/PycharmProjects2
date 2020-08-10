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
    lawyers_is_success = False
    florists_is_success = False
    dentists_is_success = False
    pet_grooming_is_success = False
    tanning_salons_is_success = False
    fitness_centers_is_success = False

    def popular_toronto(self, link):
        """
        >> This function verifies if the Popular in Toronto links are clickable and functional.
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
                driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[2]/ul/li[' + str(count) + ']/a')
            if quick_link:
                quick_link.click()
                pass
            else:
                pass

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + 'business/ON/toronto/lawyers/3844-464400.html':
                    CanPagesQuickLinks.lawyers_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + 'business/ON/toronto/florists-retail/3844-335600.html':
                    CanPagesQuickLinks.florists_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + 'business/ON/toronto/dentists/3844-239800.html':
                    CanPagesQuickLinks.dentists_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + 'business/ON/toronto/pet-washing-and-grooming/3844-606000.html':
                    CanPagesQuickLinks.pet_grooming_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + 'business/ON/toronto/tanning-salons/3844-837200.html':
                    CanPagesQuickLinks.tanning_salons_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + 'business/ON/toronto/health-clubs-and-fitness-centres/3844-405000.html':
                    CanPagesQuickLinks.fitness_centers_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_popular_toronto(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.popular_toronto(link)
        if CanPagesQuickLinks.lawyers_is_success:
            print("--> Test case for \"Lawyers\" is successful.")
        else:
            print("--> Test case for \"Lawyers\" is unsuccessful.")
        if CanPagesQuickLinks.florists_is_success:
            print("--> Test case for \"Florists\" is successful.")
        else:
            print("--> Test case for \"Florists\" is unsuccessful.")
        if CanPagesQuickLinks.dentists_is_success:
            print("--> Test case for \"Dentists\" is successful.")
        else:
            print("--> Test case for \"Dentists\" is unsuccessful.")
        if CanPagesQuickLinks.pet_grooming_is_success:
            print("--> Test case for \"Pet Grooming\" is successful.")
        else:
            print("--> Test case for \"Pet Grooming\" is unsuccessful.")
        if CanPagesQuickLinks.tanning_salons_is_success:
            print("--> Test case for \"Tanning Salons\" is successful.")
        else:
            print("--> Test case for \"Tanning Salons\" is unsuccessful.")
        if CanPagesQuickLinks.fitness_centers_is_success:
            print("--> Test case for \"Fitness Centers\" is successful.")
        else:
            print("--> Test case for \"Fitness Centers\" is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesQuickLinks(driver)
test.testing_popular_toronto(My.canpages_web_link)
