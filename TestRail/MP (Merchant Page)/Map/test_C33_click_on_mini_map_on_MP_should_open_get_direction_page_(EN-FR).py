import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def mini_map():
    """
    >> This function verifies if clicking View Map on the mini map redirects you to the direction page.
    """
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    merchant_name = My.search_clickable_webelement(first_merchant_card, By.TAG_NAME, "h3")
    assert merchant_name
    merchant_name.click()

    driver.implicitly_wait(5)

    mini_map = My.search_clickable_webelement(
    driver, By.XPATH, '//*[@id="ypgBody"]/div[3]/div/div[4]/div[2]/div[2]/div[2]/div[2]/ul/li/a')
    assert mini_map
    mini_map.click()

    url = driver.current_url[32:57]
    assert '/merchant/directions/' in url


def testing_mini_map():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/search/si/1/Restaurants/Montreal+QC")
    mini_map()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR + "/search/si/1/Restaurants/Montreal+QC")
    mini_map()
    driver.quit()
