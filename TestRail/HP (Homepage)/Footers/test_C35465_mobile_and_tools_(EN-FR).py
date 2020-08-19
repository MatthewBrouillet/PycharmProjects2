import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def mobile_and_tools(link):
    """
    >> This function verifies if the "Mobile and tools" quick links are clickable and functional
    """
    count = 1
    while count < 7:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[5]/div[2]/ul/li[" + str(count) + "]/a")

        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        url = driver.current_url
        if count == 1:
            assert link + "/applications/" in url

        elif count == 2:
            if link == My.qa_web_link:
                assert "https://twitter.com/Yellow_Pages" in url
            else:
                assert "https://twitter.com/Pages_Jaunes" in url

        elif count == 3:
            assert "https://www.facebook.com/yellowpagesgroup" in url

        elif count == 4:
            if link == My.qa_web_link:
                assert "https://edirectories.yp.ca/" in url
            else:
                assert driver.current_url == "https://eannuaires.pj.ca/" in url

        elif count == 5:
            assert link + "/fs" in url

        else:
            if link == My.qa_web_link:
                assert "https://delivery.yp.ca/optouts/address" in url
            else:
                assert "https://distribution.pj.ca/optouts/address" in url

        count += 1
        driver.back()

def testing_mobile_and_tools():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.qa_web_link
    My.search_merchant_page(driver, link)
    mobile_and_tools(link)
    print('----------')
    link = My.qa_fr_web_link
    My.search_merchant_page(driver, link)
    mobile_and_tools(link)
    driver.quit()
