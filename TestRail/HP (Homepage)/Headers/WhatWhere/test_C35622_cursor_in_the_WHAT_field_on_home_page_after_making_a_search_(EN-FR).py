import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def cursor_default_back(link):
    """
    >> This function verifies if the default position of the cursor is on the WHAT box
    >> when you go back to the home page after making a search.
    """
    # Validating that the the active element (cursor) is in the WHAT field
    assert driver.switch_to.active_element == My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']")

    # Sending keys to the "WHAT" and "WHERE" fields
    try:
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("restaurants")
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='where']").send_keys("montreal")
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
    except:
        return

    # Waiting for the result page to load
    target_page = WebDriverWait(driver, 20).until(ec.url_to_be(link + "/search/si/1/restaurants/Montreal+QC"))

    # Clicking the YP Home button to go back to the home page
    yp_home = My.search_presence_webelement(driver, By.ID, "QAypLogoLhs")
    assert yp_home and target_page
    yp_home.click()

    # Validating that the the active element (cursor) is in the WHAT field
    assert driver.switch_to.active_element == My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']")


def testing_cursor_default_back():
    """
    >> This function executes the steps of the test case
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    cursor_default_back(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    cursor_default_back(link)
    driver.quit()
