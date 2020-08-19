import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def popular_calgary(link):
    """
    >> This function verifies if the Popular in Calgary links are clickable and functional.
    """
    # Locating the Quick Links toggle
    quick_links_toggle = My.search_clickable_webelement(driver, By.XPATH, '//*[@id="footer"]/div[1]/div[1]/a[1]')
    assert quick_links_toggle
    quick_links_toggle.click()

    count = 1
    while count < 7:
        # Locating the Links container
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, '//*[@id="footer"]/div[1]/div[2]/div/div[3]/ul/li[' + str(count) + ']/a')
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page
        url = driver.current_url
        if count == 1:
            assert link + 'business/AB/calgary/dentists/91-239800.html' in url

        elif count == 2:
            assert link + 'business/AB/calgary/lawyers/91-464400.html' in url

        elif count == 3:
            assert link + 'business/AB/calgary/restaurants/91-720200.html' in url

        elif count == 4:
            assert link + 'business/AB/calgary/roofing-contractors/91-727400.html' in url

        elif count == 5:
            assert link + 'business/AB/calgary/automobile-repairing-and-service/91-052200.html' in url

        else:
            assert link + 'business/AB/calgary/electrical-contractors/91-275200.html' in url

        count += 1
        driver.back()


def testing_popular_calgary():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    popular_calgary(link)
    driver.quit()
