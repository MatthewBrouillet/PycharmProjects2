import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def relevance_click():
    relevance_button = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[1]/div/div/a")
    assert relevance_button
    relevance_button.click()


def relevance(link):
    """
    >> This function verifies if the Relevance drop down menu is clickable and functional.
    """
    global count
    count = 2
    while count < 6:
        relevance_click()

        if count == 1:
            if link[0:32] == My.qa_web_link:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Closest')
            else:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Plus proche')
        if count == 2:
            if link[0:32] == My.qa_web_link:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Highest rated')
            else:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Mieux évalués')
        if count == 3:
            if link[0:32] == My.qa_web_link:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Most reviewed')
            else:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Plus commentés')
        if count == 4:
            if link[0:32] == My.qa_web_link:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Alphabetical')
            else:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Ordre alphabétique')
        if count == 5:
            if link[0:32] == My.qa_web_link:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Recently Reviewed')
            else:
                button = My.search_clickable_webelement(driver, By.LINK_TEXT, 'Avis récent')

        assert button
        button.click()

        count = count + 1
        driver.back()


def test_relevance():
    """
    >> This function executes the steps of the test case
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link + "/search/si/1/Restaurants/Montreal+QC")
    relevance(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link + "/search/si/1/Restaurants/Montreal+QC")
    relevance(link)
    driver.quit()
