import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def popular_headings(link):
    """
    >> This function validates the headings below the search bar on the header.
    """
    count = 1
    while count < 6:

        # Locating the heading link depending on the count value
        heading_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/ul/li[" + str(count) + "]/a")
        assert heading_link
        heading_link.click()

        if count == 1:
            if link[0:32] == My.qa_web_link:
                assert driver.current_url == My.qa_web_link + '/search/si/1/Restaurants/Montreal+QC'
            else:
                assert driver.current_url == My.qa_fr_web_link + '/search/si/1/Restaurants/Montreal+QC'

        if count == 2:
            if link[0:32] == My.qa_web_link:
                assert driver.current_url == My.qa_web_link + '/search/si/1/Dentists/Montreal+QC'
            else:
                assert driver.current_url == My.qa_fr_web_link + '/search/si/1/Dentistes/Montreal+QC'

        if count == 3:
            if link[0:32] == My.qa_web_link:
                assert driver.current_url == My.qa_web_link + '/search/si/1/Medical+Clinics/Montreal+QC'
            else:
                assert driver.current_url == My.qa_fr_web_link + '/search/si/1/Cliniques+medicales/Montreal+QC'

        if count == 4:
            if link[0:32] == My.qa_web_link:
                assert driver.current_url == My.qa_web_link + '/search/si/1/Car+Repair/Montreal+QC'
            else:
                assert driver.current_url == My.qa_fr_web_link + '/search/si/1/Reparation+de+voitures/Montreal+QC'

        if count == 5:
            if link[0:32] == My.qa_web_link:
                assert driver.current_url == My.qa_web_link + '/search/si/1/Grocery+Stores/Montreal+QC'
            else:
                assert driver.current_url == My.qa_fr_web_link + '/search/si/1/Epiceries/Montreal+QC'

        count += 1


def test_popular_headings():
    """
    >> This function executes the steps of the test case
    """
    link = My.qa_web_link + "/search/si/1/restaurants/Montreal+QC"
    My.search_merchant_page(driver, link)
    popular_headings(link)
    print('----------')
    link = My.qa_fr_web_link + "/search/si/1/restaurants/Montreal+QC"
    My.search_merchant_page(driver, link)
    popular_headings(link)
    driver.quit()
