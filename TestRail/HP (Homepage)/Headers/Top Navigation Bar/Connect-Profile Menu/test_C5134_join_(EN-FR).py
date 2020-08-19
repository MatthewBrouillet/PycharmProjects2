import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def validate_join():
    """
    >> This function verifies if the join pop-up window opens
    """
    # Locating the button on the top navigation bar
    button_join = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[1]/header/div/div/div/div/div[3]/ul/li[3]")
    assert button_join
    button_join.click()

    # Validating that the pop up window is present
    window = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypModal']/div/div")
    assert window


def test_join():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link)
    validate_join()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link)
    validate_join()
    driver.quit()
