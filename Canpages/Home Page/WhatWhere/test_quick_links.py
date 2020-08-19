import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def quick_links(link):
    """
    >> This function verifies if the Quick Links are clickable and functional.
    """
    count = 1
    while count < 11:

        # Locating the quick link
        quick_link = My.search_clickable_webelement(
            driver, By.XPATH, "//*[@id='top-categories']/li[" + str(count) + "]/a")
        assert quick_link
        quick_link.click()

        # Validating the URL of the current web page
        url = driver.current_url
        if count == 1:
            assert link + "list.jsp?ct=M5H+3B7&na=Banks" in url

        elif count == 2:
            assert link + "list.jsp?ct=M5H+3B7&na=Bars" in url

        elif count == 3:
            assert link + "list.jsp?ct=M5H+3B7&na=Clinics" in url

        elif count == 4:
            assert link + "list.jsp?ct=M5H+3B7&na=Nail+Salons" in url

        elif count == 5:
            assert link + "list.jsp?ct=M5H+3B7&na=Dentists" in url

        elif count == 6:
            assert link + "list.jsp?ct=M5H+3B7&na=Florists" in url

        elif count == 7:
            assert link + "list.jsp?ct=M5H+3B7&na=Jobs" in url

        elif count == 8:
            assert link + "list.jsp?ct=M5H+3B7&na=Pharmacies" in url

        elif count == 9:
            assert link + "list.jsp?ct=M5H+3B7&na=Pizza" in url

        else:
            assert link + "list.jsp?ct=M5H+3B7&na=Restaurants" in url

        count += 1
        driver.back()


def testing_quick_links():
    """
    >> This function executes the steps of the test case
    """
    link = My.canpages_web_link
    My.search_merchant_page(driver, link)
    quick_links(link)
    driver.quit()
