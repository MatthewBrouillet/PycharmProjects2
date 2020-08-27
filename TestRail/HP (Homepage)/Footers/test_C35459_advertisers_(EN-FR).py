import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links_advertisers():
    """
    >> This function verifies if the "Advertisers" quick links are clickable and functional
    """
    count = 1
    while count < 4:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[2]/div[2]/ul/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        if count == 1:
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://business.yellowpages.ca/home/#/" in url

        elif count == 2:
            window_after = driver.window_handles[2]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://business.yellowpages.ca/onboarding/#/free-listing-yellow-pages?utm_source=ypca&utm_medium=link&utm_campaign=footer" in url

        else:
            window_after = driver.window_handles[3]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://businesscentre.yp.ca/-/fraud-preventi-1" in url

        count += 1
        window_before = driver.window_handles[0]
        driver.switch_to.window(window_before)


def testing_quick_links_advertisers():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    quick_links_advertisers()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    quick_links_advertisers()
    driver.quit()
