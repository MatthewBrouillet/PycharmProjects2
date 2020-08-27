import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def delete_previous_search(link):
    """
    >> This function verifies the functionality of the "X" (delete) toggle in the recent searches section
    """
    # Sending keys to the WHAT and WHERE fields
    try:
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("dentist")
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='where']").send_keys("montreal")
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
    except:
        return

    # Waiting for the page to load
    target_page = WebDriverWait(driver, 20).until(ec.url_to_be(link + "/search/si/1/dentist/Montreal+QC"))

    # Locating the YP home button
    yp_home = My.search_presence_webelement(driver, By.ID, "QAypLogoLhs")
    assert yp_home and target_page
    yp_home.click()

    # Selecting the previous search from the WHERE field
    where_box = My.search_presence_webelement(driver, By.ID, "where")
    assert where_box
    where_box.click()

    previous_search = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='previousLocation']/ul")
    assert previous_search
    previous_search.click()

    try:
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='whatwho']").send_keys("dentist")
        My.search_presence_webelement(driver, By.XPATH, "//*[@id='inputForm']/div[2]/div[2]/div").click()
    except:
        return


def testing_delete_previous_search():
    """
    >> This function executes the steps of the test case
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    delete_previous_search(link)
    driver.quit()
