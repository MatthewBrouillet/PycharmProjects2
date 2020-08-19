import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def cursor_what():
    """
    >> This function verifies if the default position of the cursor is on the WHAT box
    """
    # Validating that the the active element (cursor) is in the WHAT field
    assert driver.switch_to.active_element == My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']")


def test_cursor_what():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link)
    cursor_what()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link)
    cursor_what()
    driver.quit()
