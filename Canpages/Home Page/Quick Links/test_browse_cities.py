import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)

def browse_cities(link):
    """
    >> This function verifies if the Browse cities links are clickable and functional.
    """
    # Locating the Quick Links toggle
    quick_links_toggle = My.search_clickable_webelement(driver, By.XPATH, '//*[@id="footer"]/div[1]/div[1]/a[1]')
    assert quick_links_toggle
    quick_links_toggle.click()

    count = 1
    while count < 17:
        # Locating the Links container
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[1]/ul/li[' + str(count) + ']/a')
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page
        url = driver.current_url
        if count == 1:
            assert link + 'business/AB/calgary/91-directory.html' in url

        elif count == 2:
            assert link + 'business/AB/edmonton/183-directory.html' in url

        elif count == 3:
            assert link + 'business/ON/scarborough/3703-directory.html' in url

        elif count == 4:
            assert link + 'business/ON/mississagua/3453-directory.html' in url

        elif count == 5:
            assert link + 'business/BC/surrey/934-directory.html' in url

        elif count == 6:
            assert link + 'business/ON/london/3368-directory.html' in url

        elif count == 7:
            assert link + 'business/ON/ottawa/3559-directory.html' in url

        elif count == 8:
            assert link + 'business/QC/quebec/4766-directory.html' in url

        elif count == 9:
            assert link + 'business/ON/toronto/3844-directory.html' in url

        elif count == 10:
            assert link + 'business/BC/vancouver/961-directory.html' in url

        elif count == 11:
            assert link + 'business/BC/victoria/966-directory.html' in url

        elif count == 12:
            assert link + 'business/MB/winnipeg/1406-directory.html' in url

        elif count == 13:
            assert link + 'business/QC/montreal/4643-directory.html' in url

        elif count == 14:
            assert link + 'business/NS/halifax/2428-directory.html' in url

        elif count == 15:
            assert link + 'business/SK/regina/5981-directory.html' in url

        else:
            assert link + 'business/SK/saskatoon/6008-directory.html' in url

        count += 1
        driver.back()


def testing_browse_cities():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    browse_cities(link)
    driver.quit()
