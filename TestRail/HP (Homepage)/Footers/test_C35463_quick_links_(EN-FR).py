import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links(link):
    """
    >> This function verifies if the "Popular Searches" quick links are clickable and functional
    """
    count = 1
    while count < 11:

        # Locating the link
        if count == 10 and link == My.qa_fr_web_link:
            return
        else:
            pass

        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[4]/div[2]/ul/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        url = driver.current_url
        if count == 1:
            assert link + "/business" in url

        elif count == 2:
            assert link + "/locations" in url

        elif count == 3:
            if link == My.qa_web_link:
                assert link + "/neighbourhoods" in url
            else:
                assert link + "/quartiers" in url

        elif count == 4:
            assert link + "/shop/" in url

        elif count == 5:
            if link == My.qa_web_link:
                assert link + "/tips/" in url
            else:
                assert link + "/trucs/"

        elif count == 6:
            if link == My.qa_web_link:
                assert link + "/articles/loc/toronto" in url
            else:
                assert link + "/pl/loc" in url

        elif count == 7:
            if link == My.qa_web_link:
                assert link + "/pl/loc" in url
            else:
                assert link + "/pl/v/resto" in url

        elif count == 8:
            if link == My.qa_web_link:
                assert link + "/pl/v/eat" in url
            else:
                assert link + "/pl/v/magasinage" in url

        elif count == 9:
            if link == My.qa_web_link:
                assert link + "/pl/v/shop" in url
            else:
                assert link + "/pl/v/divertissement"

        else:
            assert link + "/pl/v/play" in url

        count += 1
        driver.back()


def test_quick_links():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    quick_links(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    quick_links(link)
    driver.quit()
