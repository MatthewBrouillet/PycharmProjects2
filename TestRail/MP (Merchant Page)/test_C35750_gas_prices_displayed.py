import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def has_gas_prices():
    """
    >> This function verifies if the Editors Pick is present on the merchant page.
    """
    count = 1

    # Locating the container
    container = My.search_presence_webelement(driver, By.ID, "gas")
    assert container

    # Locating the gas prices

    while count < 5:
        gas_price_displayed = My.search_presence_webelement(
            container, By.XPATH, "//*[@id='gas']/div[2]/div/div[" + str(count) + "]/div/span[1]")
        assert gas_price_displayed and gas_price_displayed is not None

        print(str(gas_price_displayed.text))
        gas_price_displayed.click()

        count += 1


def testing_has_gas_prices():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Saint-Laurent/Les-Petroles-Crevier-Inc/2483297")
    has_gas_prices()
    driver.quit()
