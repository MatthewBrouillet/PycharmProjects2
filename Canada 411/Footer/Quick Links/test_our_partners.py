import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def our_partners_quick_links(link):
    """
    >> This function verifies if the "Our partners" quick links are clickable and functional
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
    assert footer_container

    count = 1
    while count < 4:
        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[4]/li[" + str(count + 1) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        if count == 1:
            url = driver.current_url
            assert "https://www.canadaplus.ca/" in url

        elif count == 2:
            url = driver.current_url
            assert "https://www.employmentnews.com/" in url

        elif count == 3:
            url = driver.current_url
            assert "https://www.canpages.ca/" in url

        count += 1
        driver.back()

    while count < 6:
        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[5]/li[" + str(count - 2) + "]/a")
        assert quick_link
        quick_link.click()

        if count == 4:
            url = driver.current_url
            assert "https://hospitalnews.com/" in url

        elif count == 5:
            url = driver.current_url
            assert "https://mediative.com/" in url

        count += 1
        driver.back()

    while count < 8:
        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[6]/li[" + str(count - 4) + "]/a")
        assert quick_link
        quick_link.click()

        if count == 6:
            url = driver.current_url
            assert "https://www.restaurantica.com/" in url

        else:
            url = driver.current_url
            assert My.yp_web_link + '/' in url

        count += 1
        driver.back()


def test_our_partners_quick_links():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_c411_EN
    My.search_merchant_page(driver, link)
    our_partners_quick_links(link)
    driver.quit()
