import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class Canada411Home:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
               "U", "V", "W", "X", "Y", "Z"]

    def browse_people_by_name(self, link):
        """
        >> This function verifies if the "Browse by People Name" quick links are clickable and functional
        """
        # Locating the footer container
        footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[2]")
        if footer_container:
            pass
        else:
            return

        count = 1
        while count < 27:
            # print(str(count))
            # print(Canada411Home.letters[count - 1])
            # Locating the link
            quick_link = My.search_clickable_webelement(
                driver, By.XPATH, "//*[@id='c411Footer']/div[2]/ul/li[" + str(count + 1) + "]/a")
            if quick_link:
                quick_link.click()
            else:
                pass

            # Validating the URL of the current web page depending on the count
            # print(str(driver.current_url))
            if driver.current_url == link + "/" + Canada411Home.letters[count - 1] + "/":
                pass
            else:
                pass

            count += 1
            driver.back()

        Canada411Home.is_success = True

    def testing_browse_people_by_name(self, link):
        """
        >> This function will execute the test case, and takes a link as a parameter
        """
        My.search_merchant_page(driver, link)
        test.browse_people_by_name(link)
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_browse_people_by_name(My.c411_qa_web_link)
