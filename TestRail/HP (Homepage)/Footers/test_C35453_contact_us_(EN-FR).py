import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def contact_us(link):
    """
    >> This function verifies if the "Contact us" toggle is clickable
    >> and leads to "/contactus" or "/pournousjoindre"
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[2]")
    assert footer_container

    # Locating Contact us button
    contact_us_button = My.search_clickable_webelement(
        footer_container, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[1]/div[2]/a[1]")
    assert contact_us_button
    contact_us_button.click()

    # Switching to the new window
    if link == My.qa_web_link:
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
    else:
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)

    # Validating the URL of the current web page
    url = driver.current_url
    if link == My.qa_web_link:
        assert link + "/contactus" in url
    else:
        assert link + "/pournousjoindre" in url


def test_contact_us():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    contact_us(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    contact_us(link)
    driver.quit()
