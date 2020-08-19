import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def terms_of_use():
    """
    >> This function verifies if the Business Center link is clickable and functional
    """
    add_photo_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/div[2]/div/a")
    assert add_photo_button
    add_photo_button.click()

    terms_of_use_link = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgUploadPhotoForm']/div/div[7]/div[2]/label/a")
    assert terms_of_use_link
    terms_of_use_link.click()

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    print(str(driver.current_url))
    url = driver.current_url
    assert My.corporate_web_link + "legal-notice/terms-of-use-agreement/" in url


def testing_terms_of_use():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    terms_of_use()
    driver.quit()
