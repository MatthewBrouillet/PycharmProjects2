import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def has_editors_pick():
    """
    >> This function verifies if the Editors Pick is present on the merchant page.
    """
    # Locating the container
    container = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]")
    assert container

    # Locating the Editors Pick
    editors_pick = My.search_presence_webelement(
        container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/a")
    assert editors_pick.is_displayed()


def testing_has_editors_pick():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
    has_editors_pick()
    driver.quit()
