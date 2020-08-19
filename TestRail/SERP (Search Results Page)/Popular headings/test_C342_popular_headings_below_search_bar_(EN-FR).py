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

        if count == 1:
            assert heading_link.text == 'Restaurants'

        if count == 2:
            if link == My.qa_web_link + "/search/si/1/restaurants/Montreal+QC":
                assert heading_link.text == 'Dentists'
            else:
                assert heading_link.text == 'Dentistes'

        if count == 3:
            if link == My.qa_web_link + "/search/si/1/restaurants/Montreal+QC":
                assert heading_link.text == 'Medical Clinics'
            else:
                assert heading_link.text == 'Cliniques Médicales'

        if count == 4:
            if link == My.qa_web_link + "/search/si/1/restaurants/Montreal+QC":
                assert heading_link.text == 'Car Repair'
            else:
                assert heading_link.text == 'Réparation De Voitures'

        if count == 5:
            if link == My.qa_web_link + "/search/si/1/restaurants/Montreal+QC":
                assert heading_link.text == 'Grocery Stores'
            else:
                assert heading_link.text == 'Épiceries'

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
