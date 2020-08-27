import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links_about_us(link):
    """
    >> This function verifies if the "About us" quick links are clickable and functional
    """
    count = 1
    while count < 8:
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[3]/div[2]/ul/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        if count == 1:
            url = driver.current_url
            assert link + "/contactus" in url
            driver.back()

        elif count == 2:
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://jobs-emplois.yp.ca" in url

        elif count == 3:
            window_after = driver.window_handles[2]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://corporate.yp.ca/en/investors/overview/" in url

        elif count == 4:
            window_after = driver.window_handles[3]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://corporate.yp.ca/en/" in url

        elif count == 5:
            window_after = driver.window_handles[4]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://corporate.yp.ca/en/legal-notice/privacy-statement/" in url

        elif count == 6:
            window_after = driver.window_handles[5]
            driver.switch_to.window(window_after)
            url = driver.current_url
            assert "https://corporate.yp.ca/en/legal-notice/terms-of-use-agreement/" in url

        else:
            url = driver.current_url
            assert link + "/help.html" in url

        window_before = driver.window_handles[0]
        driver.switch_to.window(window_before)

        count += 1


def testing_quick_links_about_us():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    quick_links_about_us(link)
    driver.quit()
