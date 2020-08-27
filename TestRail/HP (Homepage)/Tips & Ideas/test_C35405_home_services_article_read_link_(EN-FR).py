import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def tips_ideas_home_service_links_read():
    """
    >> This function verifies if the Read link of "Home Services" in the Tips & Ideas' section is clickable
    """
    # Locating Tips and Ideas container
    tips_ideas_container = My.search_presence_webelement(driver, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]")
    assert tips_ideas_container

    # Locating Cards grid home services container
    cards_grid_home_services = My.search_presence_webelement(
        tips_ideas_container, By.XPATH, "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[1]/div")
    assert cards_grid_home_services

    # Locating the Read link of the first article
    read_link = My.search_clickable_webelement(
        cards_grid_home_services, By.XPATH,
        "//*[@id='ypgBody']/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[3]/a")
    assert read_link
    read_link.click()


def test_tips_ideas_home_service_links_read():
    """
    >> This function will execute the test case, and takes a link as a parameter
    """
    My.search_merchant_page(driver, My.Testing_Env_EN)
    tips_ideas_home_service_links_read()
    print('----------')
    My.search_merchant_page(driver, My.Testing_Env_FR)
    tips_ideas_home_service_links_read()
    driver.quit()
