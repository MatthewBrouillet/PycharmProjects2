import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YPGasPrices:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def has_gas_prices(self):
        """
        >> This function verifies if the Editors Pick is present on the merchant page.
        """
        count = 1

        # Locating the container
        container = My.search_presence_webelement(driver, By.ID, "gas")
        if container:
            pass
        else:
            return

        # Locating the gas prices

        while count < 5:
            gas_price_displayed = My.search_presence_webelement(
                container, By.XPATH, "//*[@id='gas']/div[2]/div/div[" + str(count) + "]/div/span[1]")
            if gas_price_displayed is not None:
                print(str(gas_price_displayed.text))
                gas_price_displayed.click()
                YPGasPrices.is_success = True
                pass
            else:
                pass
            count += 1


    def testing_has_gas_prices(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.has_gas_prices()
        if YPGasPrices.is_success:
            print("--> Test case for is successful.")
        else:
            print("--> Test case for is unsuccessful.")


test = YPGasPrices(driver)
test.testing_has_gas_prices(My.qa_web_link + "/bus/Quebec/Saint-Laurent/Les-Petroles-Crevier-Inc/2483297")
driver.quit()
sys.exit()
