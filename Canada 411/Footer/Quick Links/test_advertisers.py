import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def advertisers_quick_links():
    """
    >> This function verifies if the "Advertisers" quick links are clickable and functional
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]")
    assert footer_container

    # Locating the link
    quick_link = My.search_clickable_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[3]/ul[2]/li[2]/a")
    assert quick_link
    quick_link.click()

    # Validating the URL of the current web page
    url = driver.current_url
    assert "https://www.yellowpages360solution.ca/en/index.htm" in url


def testing_advertisers_quick_links():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.c411_qa_web_link)
    advertisers_quick_links()
    driver.quit()
