import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]


def browse_people_by_name(link):
    """
    >> This function verifies if the "Browse by People Name" quick links are clickable and functional
    """
    # Locating the footer container
    footer_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='c411Footer']/div[2]")
    assert footer_container

    count = 1
    while count < 27:
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='c411Footer']/div[2]/ul/li[" + str(count + 1) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        url = driver.current_url
        expected_url = link + str(letters[count - 1])
        assert expected_url in url

        count += 1
        driver.back()


def test_browse_people_by_name():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.c411_qa_web_link
    My.search_merchant_page(driver, link)
    browse_people_by_name(link)
    driver.quit()
