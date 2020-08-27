import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def upload_image_submit():
    """
    >> This function verifies if clicking on 'Add photo' opens a photo preview page
    >> that has a disabled Submit button.
    """
    add_photo_button = My.search_clickable_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/div[2]/div/a")
    assert add_photo_button
    add_photo_button.click()

    submit_button = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='imageUploadButton']")

    assert not submit_button


def testing_upload_image_submit():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    upload_image_submit()
    driver.quit()
