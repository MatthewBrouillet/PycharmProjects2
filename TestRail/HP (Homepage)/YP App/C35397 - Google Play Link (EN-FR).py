import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPApp:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def yp_app_google_play_link(self, link):
        """
        >> This function verifies if the "Google Play" link is clickable
        >> and leads to "/applications/?pid=YPmobile_home"
        """
        # Locating the YP App container
        yp_app_links_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgFooter']/div[1]/div[2]")

        # Locating the Google Play button
        if yp_app_links_container:
            google_play_button = My.search_clickable_webelement(yp_app_links_container, By.XPATH,
                                                                "//*[@id='ypgFooter']/div[1]/div[2]/a[1]/div/div")
            if google_play_button:
                google_play_button.click()
            else:
                return
        else:
            return

        # Validating the URL of the current web page
        if driver.current_url == link + "/applications/?pid=YPmobile_home":
            YPApp.is_success = True
            return
        else:
            return

    def testing_yp_app_google_play_link(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.yp_app_google_play_link(link)
        if YPApp.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")


test = YPApp(driver)
test.testing_yp_app_google_play_link(My.yp_web_link)
print('----------')
test.testing_yp_app_google_play_link(My.pj_web_link)
driver.quit()
sys.exit()
