import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def log_in_facebook():
    """
    >> This function verifies that the language toggle is clickable and functional.
    """
    # Locating the action bar
    action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
    assert action_bar

    log_in_toggle = My.search_clickable_webelement(action_bar, By.ID, 'c411YidLogin')
    assert log_in_toggle
    log_in_toggle.click()


def test_log_in_facebook():
    My.search_merchant_page(driver, My.c411_qa_web_link)
    log_in_facebook()
    driver.quit()
