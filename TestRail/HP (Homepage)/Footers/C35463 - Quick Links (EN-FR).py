import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPQuickLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    first_link_is_success = False
    second_link_is_success = False
    third_link_is_success = False
    fourth_link_is_success = False
    fifth_link_is_success = False
    sixth_link_is_success = False
    seventh_link_is_success = False
    eighth_link_is_success = False
    nineth_link_success = False
    tenth_link_is_success = False

    def quick_links(self, link):
        """
        >> This function verifies if the "Popular Searches" quick links are clickable and functional
        """
        count = 1
        while count < 11:

            # Locating the link
            if count == 10 and link == My.pj_web_link:
                return
            else:
                pass
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH,
                "//*[@id='ypgFooter']/div[2]/div[2]/div[4]/div[2]/ul/li[" + str(count) + "]/a")
            # print('Count: ' + str(count))

            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            if count == 1:
                if driver.current_url == link + "/business":
                    YPQuickLinks.first_link_is_success = True
                    pass
                else:
                    pass
            elif count == 2:
                if driver.current_url == link + "/locations":
                    YPQuickLinks.second_link_is_success = True
                    pass
                else:
                    pass
            elif count == 3:
                if link == My.yp_web_link:
                    if driver.current_url == link + "/neighbourhoods":
                        YPQuickLinks.third_link_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == link + "/quartiers":
                        YPQuickLinks.third_link_is_success = True
                        pass
                    else:
                        pass
            elif count == 4:
                if driver.current_url == link + "/shop/":
                    YPQuickLinks.fourth_link_is_success = True
                    pass
                else:
                    pass
            elif count == 5:
                if link == My.yp_web_link:
                    if driver.current_url == link + "/tips/":
                        YPQuickLinks.fifth_link_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == link + "/trucs/":
                        YPQuickLinks.fifth_link_is_success = True
                        pass
                    else:
                        pass
            elif count == 6:
                if link == My.yp_web_link:
                    if driver.current_url == link + "/articles/loc/toronto":
                        YPQuickLinks.sixth_link_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == link + "/pl/loc":
                        YPQuickLinks.sixth_link_is_success = True
                        pass
                    else:
                        pass
            elif count == 7:
                if link == My.yp_web_link:
                    if driver.current_url == link + "/pl/loc":
                        YPQuickLinks.seventh_link_is_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == link + "/pl/v/resto":
                        YPQuickLinks.seventh_link_is_success = True
                        pass
                    else:
                        pass
            elif count == 8:
                if link == My.yp_web_link:
                    if driver.current_url == link + "/pl/v/eat":
                        YPQuickLinks.eighth_link_is_success= True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == link + "/pl/v/magasinage":
                        YPQuickLinks.eighth_link_is_success = True
                        pass
                    else:
                        pass
            elif count == 9:
                if link == My.yp_web_link:
                    if driver.current_url == link + "/pl/v/shop":
                        YPQuickLinks.nineth_link_success = True
                        pass
                    else:
                        pass
                else:
                    if driver.current_url == link + "/pl/v/divertissement":
                        YPQuickLinks.nineth_link_success = True
                        pass
                    else:
                        pass
            else:
                    if driver.current_url == link + "/pl/v/play":
                        YPQuickLinks.tenth_link_is_success = True
                        pass
                    else:
                        return
            count += 1
            driver.back()

    def testing_quick_links(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.quick_links(link)
        if YPQuickLinks.first_link_is_success:
            print("-->> Test case for the first link is successful!")
        else:
            print("-->> Test case for the first link is unsuccessful!")
        if YPQuickLinks.second_link_is_success:
            print("-->> Test case for the second link is successful!")
        else:
            print("-->> Test case for the second link is unsuccessful!")
        if YPQuickLinks.third_link_is_success:
            print("-->> Test case for the third link is successful!")
        else:
            print("-->> Test case for the third link is unsuccessful!")
        if YPQuickLinks.fourth_link_is_success:
            print("-->> Test case for the fourth link is successful!")
        else:
            print("-->> Test case for the fourth link is unsuccessful!")
        if YPQuickLinks.fifth_link_is_success:
            print("-->> Test case for the fifth link is successful!")
        else:
            print("-->> Test case for the fifth link is unsuccessful!")
        if YPQuickLinks.sixth_link_is_success:
            print("-->> Test case for the sixth link is successful!")
        else:
            print("-->> Test case for the sixth link is unsuccessful!")
        if YPQuickLinks.seventh_link_is_success:
            print("-->> Test case for the seventh link is successful!")
        else:
            print("-->> Test case for the seventh link is unsuccessful!")
        if YPQuickLinks.eighth_link_is_success:
            print("-->> Test case for the eighth link is successful!")
        else:
            print("-->> Test case for the eighth link is unsuccessful!")
        if YPQuickLinks.nineth_link_success:
            print("-->> Test case for the nineth link is successful!")
        else:
            print("-->> Test case for the nineth link is unsuccessful!")
        if link == My.yp_web_link:
            if YPQuickLinks.tenth_link_is_success:
                print("-->> Test case for the tenth link is successful!")
            else:
                print("-->> Test case for the tenth link is unsuccessful!")
        else:
            return


test = YPQuickLinks(driver)
test.testing_quick_links(My.yp_web_link)
print('----------')
test.testing_quick_links(My.pj_web_link)
driver.quit()
sys.exit()
