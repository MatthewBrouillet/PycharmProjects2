import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def partners(link):
    """
    >> This function verifies if the "Partners" quick links are clickable and functional
    """
    count = 1
    while count < 3:

        # Locating the link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='ypgFooter']/div[2]/div[2]/div[6]/div[2]/ul/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page depending on the count
        url = driver.current_url
        if count == 1:
            if link == My.Testing_Env_EN:
                assert "https://www.canada411.ca/" in url
            else:
                assert "https://www.fr.canada411.ca/" in url

        else:
            if link == My.Testing_Env_EN:
                assert "https://www.canpages.ca/" in url
            else:
                assert "https://www.canpages.ca/fr/" in url

        count += 1
        driver.back()


def testing_partners():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    link = My.Testing_Env_EN
    My.search_merchant_page(driver, link)
    partners(link)
    print('----------')
    link = My.Testing_Env_FR
    My.search_merchant_page(driver, link)
    partners(link)
    driver.quit()
