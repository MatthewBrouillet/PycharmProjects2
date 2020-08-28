import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def home_button(link):
    """
    >> This function verifies that the search results are valid in regards to the keywords
    """
    # Locating the action bar
    action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
    assert action_bar

    home_button_icon = My.search_clickable_webelement(
        action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[1]/div/a')
    assert home_button
    home_button_icon.click()

    print(str(driver.current_url))
    url = driver.current_url
    assert link in url


def test_home_button():
    link = My.Testing_Env_c411_EN
    My.search_merchant_page(driver, link)
    home_button(link)
    driver.quit()

