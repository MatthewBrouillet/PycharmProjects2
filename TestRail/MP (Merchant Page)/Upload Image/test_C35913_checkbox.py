import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def checkbox():
    """
    >> This function verifies if the checkbox is clickable and functional
    """
    add_photo_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/div[2]/div/a")
    assert add_photo_button
    add_photo_button.click()

    checkbox = My.search_presence_webelement(driver, By.ID, "acceptCondition")
    assert checkbox
    checkbox.click()


def testing_checkbox():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    checkbox()
    driver.quit()
