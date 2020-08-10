import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPUploadImage:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def upload_image_browse_computer(self):
        """
        >> This function verifies if clicking on 'Add photo' opens a photo preview page
        >> that has the merchant's name.
        """
        first_merchant_card = My.search_clickable_webelement(
            driver, By.TAG_NAME, "h3")
        if first_merchant_card:
            first_merchant_card.click()
            pass
        else:
            return

        add_photo_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[3]/div/ul/li[6]/span/a")
        if add_photo_button:
            add_photo_button.click()
            pass
        else:
            return

        browse_button = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgUploadPhotoForm']/div/div[3]/button")
        if browse_button:
            browse_button.click()
            YPUploadImage.is_success = True
            return
        else:
            return

    def testing_upload_image_browse_computer(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.upload_image_browse_computer()
        if YPUploadImage.is_success:
            print("--> Test case for \"Browser computer\" is successful.")
        else:
            print("--> Test case for \"Browser computer\" is unsuccessful.")


test = YPUploadImage(driver)
test.testing_upload_image_browse_computer(My.yp_web_link + "/search/si/1/restaurants/Montreal+QC")
print('----------')
test.testing_upload_image_browse_computer(My.pj_web_link + "/search/si/1/restaurants/Montreal+QC")
driver.quit()
sys.exit()
