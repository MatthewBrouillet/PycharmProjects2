import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def share():
    """
    >> This function verifies if clicking the Share button is clickable and functional.
    """
    # Locating the container
    container = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul")
    assert container

    # Locating the Share button
    share_button = My.search_clickable_webelement(
        container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[3]")
    assert share_button
    share_button.click()

    # Locating the share drop down menu
    share_drop_down = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[3]/ul")
    assert share_drop_down


def testing_share():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
    share()
    driver.quit()
