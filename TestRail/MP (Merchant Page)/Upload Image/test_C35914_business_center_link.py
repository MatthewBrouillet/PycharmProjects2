import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def business_center():
    """
    >> This function verifies if the Business Center link is clickable and functional
    """
    add_photo_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/div[2]/div/a")
    assert add_photo_button
    add_photo_button.click()

    business_center_link = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgUploadPhotoForm']/div/div[4]/ul/li[4]/a")
    assert business_center_link
    business_center_link.click()

    url = driver.current_url
    assert "https://business.yellowpages.ca/home/#/" in url


def testing_business_center():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    business_center()
    driver.quit()
