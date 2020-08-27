import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def upload_image():
    """
    >> This function verifies if clicking on 'Add photo' opens a photo preview page
    """
    add_photo_button = My.search_clickable_webelement(
        driver, By.CSS_SELECTOR,
        "#ypgBody > div.page__container > div > div.merchant__pics > div > div:nth-child(2) > div > a")
    assert add_photo_button
    add_photo_button.click()

    photo_preview_page = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgUploadPhotoForm']/div")
    assert photo_preview_page


def testing_upload_image():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    upload_image()
    driver.quit()
