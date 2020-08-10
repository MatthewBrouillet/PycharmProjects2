import sys
import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPWidgets:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success_phone_number = False
    is_success_reserve = False
    is_success_message = False
    is_success_directions = False
    is_success_website = False

    def test_widgets(self, link):
        """
        >> This function verifies the widgets are present on the merchant page.
        """
        # Locating the container
        container = My.search_presence_webelements(
            driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li")
        if container:
            pass
        else:
            return

        # Looping through each widget
        for i in container:
            widget = My.search_clickable_webelement(i, By.TAG_NAME, "a")
            print(widget.text)
            if widget:
                if widget.text == "Phone Number":
                    YPWidgets.is_success_phone_number = True
                else:
                    pass

                if widget.text == "Reserve":
                    YPWidgets.is_success_reserve = True
                else:
                    pass

                if widget.text == "Message" or "Send Message":
                    YPWidgets.is_success_message = True
                    pass
                else:
                    pass

                if widget.text == "Directions":
                    YPWidgets.is_success_directions = True
                    pass
                else:
                    pass

                if widget.text == "Website":
                    YPWidgets.is_success_website = True
                else:
                    pass
                pass
            else:
                pass


    def testing_test_widgets(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.test_widgets(link)
        if YPWidgets.is_success_phone_number:
            print("--> Test case for \"Phone Number\" is successful.")
        else:
            print("--> Test case for \"Phone Number\" is unsuccessful.")
        if YPWidgets.is_success_reserve:
            print("--> Test case for \"Reserve\" is successful.")
        else:
            print("--> Test case for \"Reserve\" is unsuccessful.")
        if YPWidgets.is_success_message:
            print("--> Test case for \"Message\" is successful.")
        else:
            print("--> Test case for \"Message\" is unsuccessful.")
        if YPWidgets.is_success_directions:
            print("--> Test case for \"Directions\" is successful.")
        else:
            print("--> Test case for \"Directions\" is unsuccessful.")
        if YPWidgets.is_success_website:
            print("--> Test case for \"Website\" is successful.")
        else:
            print("--> Test case for \"Website\" is unsuccessful.")


test = YPWidgets(driver)
test.testing_test_widgets(My.qa_web_link + "/bus/r/Ontario/Toronto/Schnitzel-Hub-European-Bistro/7119328")
driver.quit()
sys.exit()
