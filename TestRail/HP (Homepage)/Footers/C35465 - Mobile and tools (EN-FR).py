import sys
import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMobileAndTools:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    ypca_apps_is_success = False
    follow_us_twitter_is_success = False
    facebook_fan_page_is_success = False
    yp_edirectories_is_success = False
    unknown_caller_list_is_success = False
    stop_rec_print_dir_is_success = False

    def mobile_and_tools(self, link):
        """
        >> This function verifies if the "Mobile and tools" quick links are clickable and functional
        """
        count = 1
        while count < 7:

            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH,
                "//*[@id='ypgFooter']/div[2]/div[2]/div[5]/div[2]/ul/li[" + str(count) + "]/a")

            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                if driver.current_url == link + "/applications/":
                    YPMobileAndTools.ypca_apps_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if link == My.yp_web_link:
                    if driver.current_url == "https://twitter.com/Yellow_Pages":
                        YPMobileAndTools.follow_us_twitter_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == "https://twitter.com/Pages_Jaunes":
                        YPMobileAndTools.follow_us_twitter_is_success = True
                        pass
                    else:
                        pass
            elif count == 3:
                if driver.current_url == "https://www.facebook.com/yellowpagesgroup":
                    YPMobileAndTools.facebook_fan_page_is_success = True
                    pass
                else:
                    pass
            elif count == 4:
                if link == My.yp_web_link:
                    if driver.current_url == "https://edirectories.yp.ca/":
                        YPMobileAndTools.yp_edirectories_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == "https://eannuaires.pj.ca/":
                        YPMobileAndTools.yp_edirectories_is_success = True
                        pass
                    else:
                        pass
            elif count == 5:
                if driver.current_url == link + "/fs":
                    YPMobileAndTools.unknown_caller_list_is_success = True
                    pass
                else:
                    pass
            else:
                if link == My.yp_web_link:
                    if driver.current_url == "https://delivery.yp.ca/optouts/address":
                        YPMobileAndTools.stop_rec_print_dir_is_success = True
                        return
                    else:
                        pass
                else:
                    if driver.current_url == "https://distribution.pj.ca/optouts/address":
                        YPMobileAndTools.stop_rec_print_dir_is_success = True
                        return
                    else:
                        return
            count += 1
            driver.back()

    def testing_mobile_and_tools(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.mobile_and_tools(link)
        if YPMobileAndTools.ypca_apps_is_success:
            print("-->> Test case for \"YP.ca apps\" is successful!")
        else:
            print("-->> Test case for \"YP.ca apps\" is unsuccessful!")
        if YPMobileAndTools.follow_us_twitter_is_success:
            print("-->> Test case for \"Follow us on Twitter\" is successful!")
        else:
            print("-->> Test case for \"Follow us on Twitter\" is unsuccessful!")
        if YPMobileAndTools.facebook_fan_page_is_success:
            print("-->> Test case for \"Facebook fan page\" is successful!")
        else:
            print("-->> Test case for \"Facebook fan page\" is unsuccessful!")
        if YPMobileAndTools.yp_edirectories_is_success:
            print("-->> Test case for \"YP eDirectories\" is successful!")
        else:
            print("-->> Test case for \"YP eDirectories\" is unsuccessful!")
        if YPMobileAndTools.unknown_caller_list_is_success:
            print("-->> Test case for \"Unknown caller list\" is successful!")
        else:
            print("-->> Test case for \"Unknown caller list\" is unsuccessful!")
        if YPMobileAndTools.stop_rec_print_dir_is_success:
            print("-->> Test case for \"Stop receiving the print directory\" is successful!")
        else:
            print("-->> Test case for \"Stop receiving the print directory\" is unsuccessful!")


test = YPMobileAndTools(driver)
test.testing_mobile_and_tools(My.yp_web_link)
print('----------')
test.testing_mobile_and_tools(My.pj_web_link)
driver.quit()
sys.exit()
