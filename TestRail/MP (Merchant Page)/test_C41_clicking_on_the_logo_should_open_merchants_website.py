import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def merchant_logo():
    """
    >> This function verifies if clicking on the logo leads to the merchant page.
    """
    # Locating the rating stars
    merchant_logo = My.search_presence_webelement(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[1]/div/a")
    assert merchant_logo
    merchant_logo.click()

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    print(str(driver.current_url))

    url = driver.current_url[0:23]
    assert "http://reubensdeli.com/" in url


def testing_merchant_logo():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/Quebec/Montreal/Reuben-s-Deli-and-Steakhouse/2499353.html")
    merchant_logo()
    driver.quit()
