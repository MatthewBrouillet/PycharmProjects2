import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def add_to_favourites():
    """
    >> This function verifies if clicking on 'Add to favourites' is clickable and functional.
    """
    first_merchant_card = My.search_clickable_webelement(driver, By.TAG_NAME, "h3")
    assert first_merchant_card
    first_merchant_card.click()

    add_to_favourites_button = My.search_clickable_webelement(
        driver, By.CSS_SELECTOR, "#ypgBody > div.page__container > div > "
                          "div.page__container.page__container--full.page__container--merchant > div.page__content "
                          "> div.merchant__sharebar.hide-print > ul "
                          "> li.shares__item.shares__item--fav.presenceBtnFav.jsMerchantFav > a")
    assert add_to_favourites_button
    add_to_favourites_button.click()

    connect_with_yp_container = My.search_presence_webelement(driver, By.XPATH, '//*[@id="ypModal"]/div/div')
    assert connect_with_yp_container


def testing_add_to_favourites():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/restaurants/Montreal+QC")
    add_to_favourites()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/restaurants/Montreal+QC")
    add_to_favourites()
    driver.quit()
