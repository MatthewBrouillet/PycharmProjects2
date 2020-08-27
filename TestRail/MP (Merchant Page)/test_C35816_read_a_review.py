import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def read_a_review():
    """
    >> This function verifies if the Editors Pick is present on the merchant page.
    """
    # Locating the container
    container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]")
    assert container

    # Locating the Read a review toggle
    read_a_review_toggle = My.search_presence_webelement(
        container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/a")
    assert read_a_review_toggle
    read_a_review_toggle.click()


def testing_read_a_review():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
    read_a_review()
    driver.quit()
