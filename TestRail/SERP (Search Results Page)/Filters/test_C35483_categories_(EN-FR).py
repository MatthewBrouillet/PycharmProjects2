import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def nbr_search_results():
    """
    >> This function verifies if the Categories drop down menu is clickable and functional
    """
    # Locating the Categories button
    categories_button = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/ul[2]/li/a")
    assert categories_button
    categories_button.click()

    # Locating the drop down menu
    drop_down_menu = My.search_clickable_webelement(
        driver, By.XPATH, '//*[@id="ypgBody"]/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/ul[2]/li/div')
    assert drop_down_menu


def test_nbr_search_results():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    nbr_search_results()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    nbr_search_results()
    driver.quit()
