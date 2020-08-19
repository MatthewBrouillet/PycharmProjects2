import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def advertise_with_us():
    """
    >> This function verifies that the Advertise with us toggle is clickable and functional.
    """
    # Locating the Find a Business container
    find_a_business_container = My.search_presence_webelement(
        driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]')
    assert find_a_business_container

    # Locating the More search options toggle
    advertise_with_us_toggle = My.search_clickable_webelement(
        find_a_business_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[2]/div[4]/a')
    assert advertise_with_us_toggle
    advertise_with_us_toggle.click()

    url = driver.current_url
    assert "https://www.yellowpages360solution.ca/en/index.htm" in url


def testing_advertise_with_us():
    My.search_merchant_page(driver, My.c411_qa_web_link)
    advertise_with_us()
    driver.quit()
