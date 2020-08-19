import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def lang_toggle(link_FR, link_EN):
    """
    >> This function verifies that the language toggles are clickable and functional.
    """
    # Locating the action bar
    action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
    assert action_bar

    # Locating the language toggle
    lang_toggle = My.search_clickable_webelement(
        action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[2]/ul/li[5]/span')
    assert lang_toggle
    lang_toggle.click()

    # Validating the URL of the current web page
    print(str(driver.current_url))
    url = driver.current_url
    assert link_FR in url

    time.sleep(5)

    # Locating the action bar
    action_bar = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/header/div/div')
    assert action_bar

    # Locating the language toggle
    lang_toggle = My.search_clickable_webelement(
        action_bar, By.XPATH, '//*[@id="c411Body"]/header/div/div/div[2]/ul/li[5]/span')
    assert lang_toggle
    lang_toggle.click()

    # Validating the URL of the current web page
    print(str(driver.current_url))
    url = driver.current_url
    assert link_EN in url


def testing_lang_toggle():
    link = My.c411_qa_web_link
    link_FR = My.c411_fr_qa_web_link
    link_EN = 'http://www.qa.ui.mtl.canada411.ca/'
    My.search_merchant_page(driver, link)
    lang_toggle(link_FR, link_EN)
    driver.quit()
