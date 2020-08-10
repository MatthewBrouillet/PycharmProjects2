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
    calgary_is_success = False
    edmonton_is_success = False
    scarborough_is_success = False
    mississauga_is_success = False
    surrey_is_success = False
    london_is_success = False
    ottawa_is_success = False
    quebec_city_is_success = False
    toronto_is_success = False
    vancouver_is_success = False
    victoria_is_success = False
    winnipeg_is_success = False
    montreal_is_success = False
    halifax_is_success = False
    regina_is_success = False
    saskatoon_is_success = False

    def browse_cities(self, link):
        """
        >> This function verifies if the Browse cities links are clickable and functional.
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
        while count < 17:
            # Locating the Links container
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[1]/ul/li[' + str(count) + ']/a')
            if quick_link:
                quick_link.click()
                pass
            else:
                pass

            # Validating the URL of the current web page
            if count == 1:
                if driver.current_url == link + 'business/AB/calgary/91-directory.html':
                    CanPagesQuickLinks.calgary_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + 'business/AB/edmonton/183-directory.html':
                    CanPagesQuickLinks.edmonton_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if driver.current_url == link + 'business/ON/scarborough/3703-directory.html':
                    CanPagesQuickLinks.scarborough_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if driver.current_url == link + 'business/ON/mississagua/3453-directory.html':
                    CanPagesQuickLinks.mississauga_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if driver.current_url == link + 'business/BC/surrey/934-directory.html':
                    CanPagesQuickLinks.surrey_is_success = True
                    pass
                else:
                    pass
            elif count == 6:
                if driver.current_url == link + 'business/ON/london/3368-directory.html':
                    CanPagesQuickLinks.london_is_success = True
                    pass
                else:
                    pass
            elif count == 7:
                if driver.current_url == link + 'business/ON/ottawa/3559-directory.html':
                    CanPagesQuickLinks.ottawa_is_success = True
                    pass
                else:
                    pass
            elif count == 8:
                if driver.current_url == link + 'business/QC/quebec/4766-directory.html':
                    CanPagesQuickLinks.quebec_city_is_success = True
                    pass
                else:
                    pass
            elif count == 9:
                if driver.current_url == link + 'business/ON/toronto/3844-directory.html':
                    CanPagesQuickLinks.toronto_is_success = True
                    pass
                else:
                    pass
            elif count == 10:
                if driver.current_url == link + 'business/BC/vancouver/961-directory.html':
                    CanPagesQuickLinks.vancouver_is_success = True
                    pass
                else:
                    pass
            elif count == 11:
                if driver.current_url == link + 'business/BC/victoria/966-directory.html':
                    CanPagesQuickLinks.victoria_is_success = True
                    pass
                else:
                    pass
            elif count == 12:
                if driver.current_url == link + 'business/MB/winnipeg/1406-directory.html':
                    CanPagesQuickLinks.winnipeg_is_success = True
                    pass
                else:
                    pass
            elif count == 13:
                if driver.current_url == link + 'business/QC/montreal/4643-directory.html':
                    CanPagesQuickLinks.montreal_is_success = True
                    pass
                else:
                    pass
            elif count == 14:
                if driver.current_url == link + 'business/NS/halifax/2428-directory.html':
                    CanPagesQuickLinks.halifax_is_success = True
                    pass
                else:
                    pass
            elif count == 15:
                if driver.current_url == link + 'business/SK/regina/5981-directory.html':
                    CanPagesQuickLinks.regina_is_success = True
                    pass
                else:
                    pass
            else:
                if driver.current_url == link + 'business/SK/saskatoon/6008-directory.html':
                    CanPagesQuickLinks.saskatoon_is_success = True
                    return
                else:
                    return
            count += 1
            driver.back()

    def testing_browse_cities(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.browse_cities(link)
        if CanPagesQuickLinks.calgary_is_success:
            print("--> Test case for \"Calgary\" is successful.")
        else:
            print("--> Test case for \"Calgary\" is unsuccessful.")
        if CanPagesQuickLinks.edmonton_is_success:
            print("--> Test case for \"Edmonton\" is successful.")
        else:
            print("--> Test case for \"Edmonton\" is unsuccessful.")
        if CanPagesQuickLinks.scarborough_is_success:
            print("--> Test case for \"Scarborough\" is successful.")
        else:
            print("--> Test case for \"Scarborough\" is unsuccessful.")
        if CanPagesQuickLinks.mississauga_is_success:
            print("--> Test case for \"Mississauga\" is successful.")
        else:
            print("--> Test case for \"Mississauga\" is unsuccessful.")
        if CanPagesQuickLinks.surrey_is_success:
            print("--> Test case for \"Surrey\" is successful.")
        else:
            print("--> Test case for \"Surrey\" is unsuccessful.")
        if CanPagesQuickLinks.london_is_success:
            print("--> Test case for \"London\" is successful.")
        else:
            print("--> Test case for \"London\" is unsuccessful.")
        if CanPagesQuickLinks.ottawa_is_success:
            print("--> Test case for \"Ottawa\" is successful.")
        else:
            print("--> Test case for \"Ottawa\" is unsuccessful.")
        if CanPagesQuickLinks.quebec_city_is_success:
            print("--> Test case for \"Quebec City\" is successful.")
        else:
            print("--> Test case for \"Quebec City\" is unsuccessful.")
        if CanPagesQuickLinks.toronto_is_success:
            print("--> Test case for \"Toronto\" is successful.")
        else:
            print("--> Test case for \"Toronto\" is unsuccessful.")
        if CanPagesQuickLinks.vancouver_is_success:
            print("--> Test case for \"Vancouver\" is successful.")
        else:
            print("--> Test case for \"Vancouver\" is unsuccessful.")
        if CanPagesQuickLinks.victoria_is_success:
            print("--> Test case for \"Victoria\" is successful.")
        else:
            print("--> Test case for \"Victoria\" is unsuccessful.")
        if CanPagesQuickLinks.winnipeg_is_success:
            print("--> Test case for \"Winnipeg\" is successful.")
        else:
            print("--> Test case for \"Winnipeg\" is unsuccessful.")
        if CanPagesQuickLinks.montreal_is_success:
            print("--> Test case for \"Montreal\" is successful.")
        else:
            print("--> Test case for \"Montreal\" is unsuccessful.")
        if CanPagesQuickLinks.halifax_is_success:
            print("--> Test case for \"Halifax\" is successful.")
        else:
            print("--> Test case for \"Halifax\" is unsuccessful.")
        if CanPagesQuickLinks.regina_is_success:
            print("--> Test case for \"Regina\" is successful.")
        else:
            print("--> Test case for \"Regina\" is unsuccessful.")
        if CanPagesQuickLinks.saskatoon_is_success:
            print("--> Test case for \"Saskatoon\" is successful.")
        else:
            print("--> Test case for \"Saskatoon\" is unsuccessful.")
        driver.quit()
        sys.exit()


test = CanPagesQuickLinks(driver)
test.testing_browse_cities(My.canpages_web_link)
