import re
import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class YellowPages:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False
    failed_search = []
    page_count = 1
    total_result_count = 0
    failed_count = 0

    def is_valid_search(self):
        """
        >> This function verifies that the search results are valid in regards to the keywords
        """
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
                YellowPages.failed_count += 1
                YellowPages.failed_search.append(header)
            YellowPages.total_result_count += 1
            result_per_page_count += 1

        # Locating the "Next" button
        if YellowPages.page_count == 1:
            has_next_page = My.search_clickable_webelement(
                driver, By.CSS_SELECTOR,
                "#ypgBody > div.page__container.jsTabsContent.page__container--right-sidebar.hasMap > div > "
                "div.page__content.jsListingMerchantCards.jsListContainer > "
                "div.resultList.jsResultsList.jsMLRContainer > div.view_more_section_noScroll > a")
        else:
            has_next_page = My.search_clickable_webelement(
                driver, By.CSS_SELECTOR,
                "#ypgBody > div.page__container.jsTabsContent.page__container--right-sidebar.hasMap > div > "
                "div.page__content.jsListingMerchantCards.jsListContainer > "
                "div.resultList.jsResultsList.jsMLRContainer > div.view_more_section_noScroll > a:nth-child(3)")

        # Verifying if there is a next page to look through
        if bool(has_next_page):
            has_next_page.click()
            YellowPages.page_count += 1
            return self.is_valid_search()
        else:
            # Verifying if there are any failed results
            if YellowPages.failed_count == 0:
                YellowPages.is_success = True
                return
            else:
                print("List of failed results: " + str(YellowPages.failed_search))
                return

    def testing_lawyers(self, link, what, where):
        """
        >> This function will execute the test case, and takes a link, a keyword and a location as parameters
        """
        My.search_merchant_param(driver, link, what, where)
        test.is_valid_search()
        if YellowPages.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = YellowPages(driver)
test.testing_lawyers(My.qa_web_link, "lawyers", "montreal")
