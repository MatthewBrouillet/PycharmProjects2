import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def related_articles():
    """
    >> This function verifies if the first article of the 'Related Articles' is clickable and functional
    """
    # Locating the container
    container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/div[2]")
    assert container

    # Locating the Related Articles button
    related_articles_button = My.search_clickable_webelement(
            container, By.XPATH,
            "//*[@id='ypgBody']/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/a")
    assert related_articles_button
    related_articles_button.click()


def testing_related_articles():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.qa_web_link + '/search/si/1/restaurants/Montreal+QC')
    related_articles()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + '/search/si/1/restaurants/Montreal+QC')
    related_articles()
    driver.quit()
