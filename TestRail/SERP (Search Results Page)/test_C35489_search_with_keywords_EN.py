import re
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def is_valid_search():
    """
    >> This function verifies that the search results are valid in regards to the keywords
    """
    # Variables
    failed_search = []
    total_result_count = 0
    failed_count = 0

    result_per_page_count = 1
    # Verifying if all individual result containers on the page are present
    containers = My.search_presence_webelements(driver, By.CLASS_NAME, "listing_right_section")

    for i in containers:
        container_content = My.search_presence_webelement(
            i, By.XPATH,
            "//*[@id='ypgBody']/div[2]/div/div[1]/div[8]/div[1]/div[" + str(result_per_page_count) +
            "]/div/div/div/div[2]/div[1]/div[1]")

        # Regex
        x = re.search(r"Law", container_content.text)
        # Retrieving the header of the individual search results
        header = My.search_presence_webelement(i, By.TAG_NAME, "h3").get_attribute('textContent')

        # Verifying if the content of the search result matches the regex
        if bool(x):
            pass
        else:
            failed_count += 1
            failed_search.append(header)
        total_result_count += 1
        result_per_page_count += 1

    # Verifying if there are any failed results
    assert failed_count == 0
    print("List of failed results: " + str(failed_search))


def testing_lawyers():
    """
    >> This function will execute the test case, and takes a link, a keyword and a location as parameters
    """
    My.search_merchant_param(driver, My.Testing_Env_EN, "lawyers", "montreal")
    is_valid_search()
    driver.quit()
