import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def related_content():
    """
    >> This function verifies if the first link of 'Related Content' is clickable and functional.
    """
    # Locating the container
    related_content_container = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="ypgBody"]/div[2]/div/div[2]/div[2]/div[8]/div[2]')
    assert related_content_container

    # Locating the first Related content link
    related_content_first_link = My.search_clickable_webelement(
        related_content_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/div[2]/div[8]/div[2]/ul/li[1]/a")
    assert related_content_first_link

    webdriver.ActionChains(driver).move_to_element(related_content_first_link).click(related_content_first_link).perform()


def testing_related_content():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/restaurants/Montreal+QC")
    related_content()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/restaurants/Montreal+QC")
    related_content()
    driver.quit()
