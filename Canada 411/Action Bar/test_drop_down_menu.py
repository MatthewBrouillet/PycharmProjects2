import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def drop_down_menu():
    """
    >> This function verifies that the search results are valid in regards to the keywords
    """
    # Locating the action bar
    action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
    assert action_bar

    drop_down_menu = My.search_clickable_webelement(
        action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[1]/a')
    assert drop_down_menu
    drop_down_menu.click()

    side_menu = My.search_presence_webelement(driver, By.XPATH, '/html/body/div[4]')
    assert side_menu


def test_drop_down_menu():
    My.search_merchant_page(driver, My.Testing_Env_c411_EN)
    drop_down_menu()
    driver.quit()

