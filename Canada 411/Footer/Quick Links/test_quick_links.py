import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links(link):
    """
    >> This function verifies if the "Quick links" quick links are clickable and functional
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
    assert footer_container

    count = 1
    while count < 5:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[3]/li[" + str(count + 1) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        if count == 1:
            url = driver.current_url
            assert link + "help.html?key=faq" in url

        elif count == 2:
            url = driver.current_url
            assert link + "help.html" in url

        elif count == 3:
            url = driver.current_url
            assert "https://lnnte-dncl.gc.ca/" in url

        elif count == 4:
            url = driver.current_url
            assert "https://delivery.yp.ca/" in url

        count += 1
        driver.back()


def test_quick_links():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_c411_EN
    My.search_merchant_page(driver, link)
    quick_links(link)
    driver.quit()
