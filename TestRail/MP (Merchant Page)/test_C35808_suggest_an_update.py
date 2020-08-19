import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def suggest_an_update():
    """
    >> This function verifies if clicking the Suggest an Update button is clickable and functional.
    """
    # Locating the container
    container = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul")
    assert container

    # Locating the Suggest an Update button
    suggest_an_update_button = My.search_clickable_webelement(
        container, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[4]/div[2]/div[6]/ul/li[4]/button")
    assert suggest_an_update_button
    suggest_an_update_button.click()

    # Locating the Suggest an Update popup window
    suggest_popup = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypSuggestUpdateOwner']/div/div")
    assert suggest_popup


def testing_suggest_an_update():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Chalet-Bar-B-Q/3391918")
    suggest_an_update()
    driver.quit()
