import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def mobile_tools_more_quick_links():
    """
    >> This function verifies if the "Mobile, tools and more" quick links are clickable and functional
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
    assert footer_container

    count = 1
    while count < 3:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[2]/li[" + str(count + 3) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        if count == 1:
            url = driver.current_url
            assert "https://www.yellowpages.ca/applications/" in url

        elif count == 2:
            print(str(driver.current_url))
            url = driver.current_url
            assert "https://shopwise.yp.ca/" in url

        count += 1
        driver.back()


def testing_mobile_tools_more_quick_links():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.c411_qa_web_link)
    mobile_tools_more_quick_links()
    driver.quit()
