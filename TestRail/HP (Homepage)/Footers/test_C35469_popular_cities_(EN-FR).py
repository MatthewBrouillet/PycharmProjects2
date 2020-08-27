import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def popular_cities(link):
    """
    >> This function verifies if the "Popular Cities" quick links are clickable and functional
    """
    count = 1
    while count < 11:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[1]/div[4]/ul/li[" + str(count) + "]/a")

        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        url = driver.current_url
        if link == My.Testing_Env_EN:
            if count == 1:
                assert link + "/locations/Alberta/Calgary" in url

            elif count == 2:
                assert link + "/locations/Alberta/Edmonton" in url

            elif count == 3:
                assert link + "/locations/Quebec/Gatineau" in url

            elif count == 4:
                assert link + "/locations/Ontario/Hamilton" in url

            elif count == 5:
                assert link + "/locations/Ontario/Toronto" in url

            elif count == 6:
                assert link + "/locations/Manitoba/Winnipeg" in url

            elif count == 7:
                if link == My.Testing_Env_EN:
                    assert link + "/locations/British-Columbia/Vancouver" in url
                else:
                    assert link + "/locations/Colombie-Britannique/Vancouver" in url

            elif count == 8:
                assert link + "/locations/Quebec/Montreal" in url

            elif count == 9:
                assert link + "/locations/Ontario/Ottawa" in url

            else:
                assert link + "/locations/Quebec/Quebec" in url

        count += 1
        driver.back()


def testing_popular_cities():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    popular_cities(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    popular_cities(link)
    driver.quit()
