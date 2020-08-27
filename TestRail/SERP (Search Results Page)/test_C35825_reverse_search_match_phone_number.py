import time
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def is_valid_search():
    """
    >> This function verifies if the search results are relevant to the entered key (in this case, phone number)
    """
    # Variables
    results_phone, results_header, results_failure = [], [], []
    page_count = 1

    # Locating all individual result containers on the page
    containers = My.search_presence_webelements(driver, By.CLASS_NAME, "listing_right_section")

    for i in containers:
        header = My.search_presence_webelement(i, By.TAG_NAME, "a").text
        phone = My.search_presence_webelement(i, By.TAG_NAME, "h4").get_attribute('textContent')
        results_header.append(header)
        results_phone.append(phone)

    # Verifying the validity of the results
    assert results_phone

    for phone in results_phone:
        if phone == '514-848-2424':
            pass
        else:
            results_failure.append(phone)

    # Locating the "Next" button
    if page_count == 1:
        has_next_page = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[7]/div[2]/a")
    else:
        has_next_page = My.search_presence_webelement(
            driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div/div[1]/div[7]/div[2]/a[2]")

    if bool(has_next_page):
        has_next_page.click()
        page_count += 1
        return is_valid_search()
    else:
        assert len(results_failure) == 0
        print("List of failed results: " + str(results_failure))


def testing_phone_numbers():
    """
    >> This function will execute the test case, and takes a link, a phone number and a location as parameters
    """
    My.search_merchant_param(driver, My.Testing_Env_EN, "5148482424", "Toronto")
    is_valid_search()
    driver.quit()
