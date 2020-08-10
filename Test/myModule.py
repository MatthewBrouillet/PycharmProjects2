import sys
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# URLs
global yp_web_link, qa_web_link, pj_web_link, c411_web_link, c411_fr_web_link, c411_qa_web_link, c411_fr_qa_web_link, \
    corporate_web_link, sit_web_link, entreprise_web_link, canpages_web_link, canpages_fr_web_link
qa_web_link = "https://qa-ui-mtl.yellowpages.ca"
yp_web_link = "https://www.yellowpages.ca"
pj_web_link = "https://www.pagesjaunes.ca"
c411_web_link = "https://www.canada411.ca"
c411_fr_web_link = "https://www.fr.canada411.ca"
c411_qa_web_link = "https://www.qa.ui.mtl.canada411.ca/"
c411_fr_qa_web_link = 'http://www.fr.qa.ui.mtl.canada411.ca/'
sit_web_link = "http://ypgldcypui-sit01.itops.ad.ypg.com/"
corporate_web_link = "https://corporate.yp.ca/en/"
entreprise_web_link = "https://entreprise.pj.ca/fr/"
canpages_web_link = "https://www.canpages.ca/"
canpages_fr_web_link = "https://www.canpages.ca/fr/"


# Function for YP Quick Links
def search_smart_links(driver, link):
    """
    >> This function redirects you to the Smart Links page on yp.ca
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='ypgFooter']/div[2]/div[2]/div[4]/div[1]/span").click()
        driver.find_element_by_xpath("//*[@id='ypgFooter']/div[2]/div[2]/div[4]/div[2]/ul/li[7]/a").click()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


def search_quick_links(driver, link, path):
    """
    >> This function redirects you to one of the Quick Links on the page on yp.ca
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_xpath(path).click()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


def goto_smart_link_city(driver, by, path):
    # Function that locates the Smart Link for a city and redirects you to that city's page
    city_link = search_clickable_webelement(driver, by, path)
    if bool(city_link):
        city_link.click()
        return True
    else:
        return False


def goto_first_smart_link(driver, by, path):
    # Function that locates the City's first Smart Link and redirects you to that specific page
    first_link = search_presence_webelement(driver, by, path)
    if bool(first_link):
        first_link.click()
        return True
    else:
        return False


def eat_link(driver, by):
    # Function that verifies if the Eat, Shop and Play button for every city (in Smart links) is clickable
    eat_link = search_clickable_webelement(
        driver, by, "//*[@id='ypgBody']/div[1]/header/div/div/div/div[2]/div/ul/li[3]/a")
    if bool(eat_link):
        eat_link.click()
        if goto_first_smart_link(driver, by, "//h2//a"):
            pass
        else:
            print("No links are present under \"Eat\"")
        driver.execute_script("window.history.go(-1)")
        return True
    else:
        return False


def shop_link(driver, by):
    shop_link = search_clickable_webelement(
        driver, by, "//*[@id='ypgBody']/div[1]/header/div/div/div/div[2]/div/ul/li[4]/a")
    if bool(shop_link):
        shop_link.click()
        if goto_first_smart_link(driver, by, "//h2//a"):
            pass
        else:
            print("No links are present under \"Shop\"")
        driver.execute_script("window.history.go(-1)")
        return True
    else:
        return False


def play_link(driver, by):
    play_link = search_clickable_webelement(
        driver, by, "//*[@id='ypgBody']/div[1]/header/div/div/div/div[2]/div/ul/li[5]/a")
    if bool(play_link):
        play_link.click()
        if goto_first_smart_link(driver, by, "//h2//a"):
            pass
        else:
            print("No links are present under \"Play\"")
        driver.execute_script("window.history.go(-1)")
        return True
    else:
        return False


# Functions for searching merchant pages on canada411 website
def search_411_reverse_person(driver, link, phone):
    """
    >> This function searches on the canada411 website by sending specific keys to the search engine
    >> and maximizes the web browser window
    >> If the web browser cannot be accessed due to an error, the program is terminated
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_id("c411PeopleReverseWhat").send_keys(phone)
        driver.find_element_by_id("c411PeopleReverseFind").click()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


def search_411_reverse_business(driver, link, phone):
    """
    >> This function searches on the canada411 website by sending specific keys to the search engine
    >> and maximizes the web browser window
    >> If the web browser cannot be accessed due to an error, the program is terminated
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_id("c411BusinessReverseWhat").send_keys(phone)
        driver.find_element_by_id("c411BusinessReverseFind").click()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


def search_411_person(driver, link, who, where):
    """
    >> This function searches on the canada411 website by sending specific keys to the search engine
    >> and maximizes the web browser window
    >> If the web browser cannot be accessed due to an error, the program is terminated
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_id("c411PeopleWhat").send_keys(who)
        driver.find_element_by_id("c411PeopleWhere").send_keys(where)
        driver.find_element_by_id("c411PeopleFind").click()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


def search_411_business(driver, link, what, where):
    """
    >> This function searches on the canada411 website by sending specific keys to the search engine
    >> and maximizes the web browser window
    >> If the web browser cannot be accessed due to an error, the program is terminated
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_id("c411BusinessWhat").send_keys(what)
        driver.find_element_by_id("c411BusinessWhere").send_keys(where)
        driver.find_element_by_id("c411BusinessFind").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


# Functions for searching merchant pages on canpages website
def search_canpages_param(driver, link, what, where):
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_id("search-term-input").send_keys(what)
        driver.find_element_by_id("location-field-view").send_keys(where)
        driver.find_element_by_id("business-search-form-submit").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()

# Functions for searching merchant pages on YP website
def search_merchant_page(driver, link):
    """
    >> This function searches for the merchant's page and maximizes the web browser window
    >> If the web browser cannot be accessed due to an error, the program is terminated
    """
    try:
        driver.get(link)
        driver.maximize_window()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


def search_merchant_param(driver, link, what, where):
    """
    >> This function searches on the YP website by sending specific keys to the search engine
    >> and maximizes the web browser window
    >> If the web browser cannot be accessed due to an error, the program is terminated
    """
    try:
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_id("whatwho").send_keys(what)
        driver.find_element_by_id("where").send_keys(where)
        driver.find_element_by_xpath("//*[@id='inputForm']/div[2]/div[2]/div/button/span[1]").click()
        time.sleep(5)
    except:
        print("-->> An error occurred. Exiting program!")
        print("Test case is unsuccessful")
        driver.quit()
        sys.exit()


# Functions for WebElements
def search_presence_webelement(driver, by, path):
    try:
        return WebDriverWait(driver, 5).until(ec.presence_of_element_located((by, path)))
    except TimeoutException:
        print("-->> A \"Timeout Exception\" was thrown.")
        pass
    except NoSuchElementException:
        print("-->> A \"NoSuchElement Exception\" was thrown.")
        pass
    except:
        print("-->> An error occurred.")
        pass


def search_presence_webelements(driver, by, path):
    try:
        return WebDriverWait(driver, 5).until(ec.presence_of_all_elements_located((by, path)))
    except TimeoutException:
        print("-->> A \"Timeout Exception\" was thrown.")
        pass
    except NoSuchElementException:
        print("-->> A \"NoSuchElement Exception\" was thrown.")
        pass
    except:
        print("-->> An error occurred.")
        pass


def search_visibility_webelement(driver, by, path):
    try:
        return WebDriverWait(driver, 5).until(ec.visibility_of_element_located((by, path)))
    except TimeoutException:
        print("-->> A \"Timeout Exception\" was thrown.")
        pass
    except NoSuchElementException:
        print("-->> A \"NoSuchElement Exception\" was thrown.")
        pass
    except:
        print("-->> An error occurred.")
        pass


def search_clickable_webelement(driver, by, path):
    try:
        return WebDriverWait(driver, 5).until(ec.element_to_be_clickable((by, path)))
    except TimeoutException:
        print("-->> A \"Timeout Exception\" was thrown.")
        pass
    except NoSuchElementException:
        print("-->> A \"NoSuchElement Exception\" was thrown.")
        pass
    except:
        print("-->> An error occurred.")
        pass
