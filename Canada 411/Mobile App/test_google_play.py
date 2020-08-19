import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def google_play():
    """
    >> This function verifies that the Google Play button is clickable and functional.
    """
    # Locating the Mobile App container
    mobile_app_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]')
    assert mobile_app_container

    # Locating the Google Play button
    google_play_button = My.search_clickable_webelement(
        mobile_app_container, By.XPATH, '//*[@id="c411Body"]/div[2]/div[2]/div/div[2]/ul/li[2]/a')
    assert google_play_button
    google_play_button.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert "https://play.google.com/store/apps/" in url


def test_google_play():
    My.search_merchant_page(driver, My.c411_qa_web_link)
    google_play()
    driver.quit()
