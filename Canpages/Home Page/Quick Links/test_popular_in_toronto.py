import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def popular_toronto(link):
    """
    >> This function verifies if the Popular in Toronto links are clickable and functional.
    """
    # Locating the Quick Links toggle
    quick_links_toggle = My.search_clickable_webelement(driver, By.XPATH, '//*[@id="footer"]/div[1]/div[1]/a[1]')
    assert quick_links_toggle
    quick_links_toggle.click()

    count = 1
    while count < 7:
        # Locating the Links container
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[2]/ul/li[' + str(count) + ']/a')
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page
        url = driver.current_url
        if count == 1:
            assert link + 'business/ON/toronto/lawyers/3844-464400.html' in url

        elif count == 2:
            assert link + 'business/ON/toronto/florists-retail/3844-335600.html' in url

        elif count == 3:
            assert link + 'business/ON/toronto/dentists/3844-239800.html' in url

        elif count == 4:
            assert link + 'business/ON/toronto/pet-washing-and-grooming/3844-606000.html' in url

        elif count == 5:
            assert link + 'business/ON/toronto/tanning-salons/3844-837200.html' in url

        else:
            assert link + 'business/ON/toronto/health-clubs-and-fitness-centres/3844-405000.html' in url

        count += 1
        driver.back()


def testing_popular_toronto():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    popular_toronto(link)
    driver.quit()
