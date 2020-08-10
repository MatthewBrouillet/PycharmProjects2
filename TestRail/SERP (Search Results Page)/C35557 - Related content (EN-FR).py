import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPRelatedContent:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def related_content(self):
        """
        >> This function verifies if the first link of 'Related Content' is clickable and functional.
        """
        # Locating the container
        related_content_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="ypgBody"]/div[2]/div/div[2]/div[2]/div[8]/div[2]')
        if related_content_container:
            pass
        else:
            return

        # Locating the first Related content link
        related_content_first_link = My.search_clickable_webelement(
            related_content_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[2]/div[2]/div[8]/div[2]/ul/li[1]/a")

        if related_content_first_link:
            webdriver.ActionChains(driver).move_to_element(related_content_first_link).click(
                related_content_first_link).perform()
        else:
            print('Link does not work')
            return

        YPRelatedContent.is_success = True

    def testing_related_content(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.related_content()
        if YPRelatedContent.is_success:
            print("--> Test case for \"Related Content link\" is successful.")
        else:
            print("--> Test case for \"Related Content link\" is unsuccessful.")


test = YPRelatedContent(driver)
test.testing_related_content(My.yp_web_link + "/search/si/1/restaurants/Montreal+QC")
print('----------')
test.testing_related_content(My.pj_web_link + "/search/si/1/restaurants/Montreal+QC")
driver.quit()
sys.exit()
