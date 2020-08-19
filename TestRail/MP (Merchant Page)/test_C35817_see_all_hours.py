import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def see_all_hours():
    """
    >> This function verifies if the Editors Pick is present on the merchant page.
    """
    # Locating the container
    container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]")
    assert container

    # Locating the Read a review toggle
    see_all_hours_toggle = My.search_presence_webelement(
        container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/span/a")
    assert see_all_hours_toggle
    see_all_hours_toggle.click()

    hours_container = My.search_presence_webelement(driver, By.ID, 'openHours')
    assert hours_container


def testing_see_all_hours():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
    see_all_hours()
    driver.quit()
