import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links_popular_searches(link):
    """
    >> This function verifies if the "Popular Searches" quick links are clickable and functional
    """
    count = 1
    while count < 11:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[1]/div[2]/ul/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        url = driver.current_url
        if count == 1:
            assert link + "/business/01125710.html" in url

        elif count == 2:
            assert link + "/business/01012401.html" in url

        elif count == 3:
            assert link + "/business/00126870.html" in url

        elif count == 4:
            assert "/business/00135600.html" in url

        elif count == 5:
            assert link + "/business/00682205.html" in url

        elif count == 6:
            assert link + "/business/00681600.html" in url

        elif count == 7:
            assert link + "/business/00304200.html" in url

        elif count == 8:
            assert link + "/business/90010010.html" in url

        elif count == 9:
            assert link + "/business/00414600.html" in url

        else:
            assert driver.current_url == link + "/business/00761600.html" in url

        count += 1
        driver.back()


def test_quick_links_popular_searches():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    quick_links_popular_searches(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    quick_links_popular_searches(link)
    driver.quit()
