import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links(link):
    """
    >> This function verifies if the quick link are clickable
    >> and leads to the right URL
    """
    count = 1
    while count < 6:

        # Locating the toggle
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page
        if count == 1:
            url = driver.current_url
            assert link + "/search/si/1/Restaurants/Montreal+QC" in url

        elif count == 2:
            url = driver.current_url
            if link == My.qa_web_link:
                assert link + "/search/si/1/Dentists/Montreal+QC" in url
            else:
                assert link + "/search/si/1/Dentistes/Montreal+QC" in url

        elif count == 3:
            url = driver.current_url
            if link == My.qa_web_link:
                assert link + "/search/si/1/Medical+Clinics/Montreal+QC" in url
            else:
                assert link + "/search/si/1/Cliniques+medicales/Montreal+QC" in url

        elif count == 4:
            url = driver.current_url
            if link == My.qa_web_link:
                assert link + "/search/si/1/Car+Repair/Montreal+QC" in url
            else:
                assert link + "/search/si/1/Reparation+de+voitures/Montreal+QC" in url

        else:
            url = driver.current_url
            if link == My.qa_web_link:
                assert link + "/search/si/1/Grocery+Stores/Montreal+QC" in url
            else:
                assert link + "/search/si/1/Epiceries/Montreal+QC" in url

        count += 1
        driver.back()


def test_quick_links():
    """
    >> This function executes the steps of the test case
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    quick_links(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    quick_links(link)
    driver.quit()
