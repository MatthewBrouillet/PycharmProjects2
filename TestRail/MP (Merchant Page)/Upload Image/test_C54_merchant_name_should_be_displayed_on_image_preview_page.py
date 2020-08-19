import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def upload_image_merchant_name():
    """
    >> This function verifies if clicking on 'Add photo' opens a photo preview page
    >> that has the merchant's name.
    """
    add_photo_button = My.search_clickable_webelement(
        driver, By.CSS_SELECTOR,
        "#ypgBody > div.page__container > div > div.merchant__pics > div > div:nth-child(2) > div > a")
    assert add_photo_button
    add_photo_button.click()

    merchant_name = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgUploadPhotoForm']/div/div[1]/a")
    assert merchant_name
    print(merchant_name.text)


def testing_upload_image_merchant_name():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    upload_image_merchant_name()
    driver.quit()
