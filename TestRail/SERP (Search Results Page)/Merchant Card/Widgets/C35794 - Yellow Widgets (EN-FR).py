import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPMerchantCardLinks:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False
    successful_search = []

    def merchant_card_yellow_widgets(self):
        """
        >> This function verifies if the yellow widgets on the merchant card are present and clickable.
        """
        # Locating the first merchant card
        first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
        if first_merchant_card:
            pass
        else:
            return

        # Validating the yellow widgets
        yellow_widgets_container = My.search_presence_webelement(
            first_merchant_card, By.CLASS_NAME, "listing__mlr__root")
        if yellow_widgets_container:
            widgets = My.search_presence_webelements(yellow_widgets_container, By.CLASS_NAME, "serpMessage")

            # Validating if some of the yellow widgets are present
            for i in widgets:
                if i.text != '':
                    print(i.text)
                    YPMerchantCardLinks.successful_search.append(i)
                if len(YPMerchantCardLinks.successful_search) > 0:
                    YPMerchantCardLinks.is_success = True
                else:
                    return
        else:
            return

    def testing_merchant_card_yellow_widgets(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.merchant_card_yellow_widgets()
        if YPMerchantCardLinks.is_success:
            print("--> Test case is successful.")
        else:
            print("--> Test case is unsuccessful.")


test = YPMerchantCardLinks(driver)
test.testing_merchant_card_yellow_widgets(My.yp_web_link + "/search/si/1/Restaurants/Montreal+QC")
print('----------')
test.testing_merchant_card_yellow_widgets(My.pj_web_link + "/search/si/1/Restaurants/Montreal+QC")
driver.quit()
sys.exit()
