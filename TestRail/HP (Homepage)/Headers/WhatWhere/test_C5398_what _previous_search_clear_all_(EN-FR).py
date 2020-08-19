import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def clear_previous_searches(link):
    """
    >> This function verifies the functionality of the "Clear all" toggle in the "where" box
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

    # Locating the WHERE field
    where_box = My.search_presence_webelement(driver, By.ID, "where")
    assert where_box
    where_box.click()

    # Locating the Clear All toggle
    clear_all = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='previousLocation']/h2/span[2]")
    assert clear_all
    clear_all.click()

    # Clearing all the previous searches
    clear_message = My.search_presence_webelement(driver, By.XPATH, "//*[@id='previousLocation']/p")

    if link == My.qa_web_link:
        assert clear_message and clear_message.get_attribute("textContent") == "Your recent locations have been cleared"
    else:
        assert clear_message and clear_message.get_attribute("textContent") == \
               "Vos emplacements récents ont été effacés"


def testing_clear_previous_searches():
    """
    >> This function executes the steps of the test case
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    clear_previous_searches(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    clear_previous_searches(link)
    driver.quit()
