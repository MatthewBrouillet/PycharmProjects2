import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def merchant_card_yellow_widgets():
    """
    >> This function verifies if the yellow widgets on the merchant card are present and clickable.
    """
    global successful_search
    successful_search = []

    # Locating the first merchant card
    first_merchant_card = My.search_presence_webelement(driver, By.CLASS_NAME, "listing__content__wrapper")
    assert first_merchant_card

    # Validating the yellow widgets
    yellow_widgets_container = My.search_presence_webelement(first_merchant_card, By.CLASS_NAME, "listing__mlr__root")
    assert yellow_widgets_container

    widgets = My.search_presence_webelements(yellow_widgets_container, By.CLASS_NAME, "serpMessage")
    assert widgets

    # Validating if some of the yellow widgets are present
    for i in widgets:
        if i.text != '':
            print(i.text)
            successful_search.append(i)
            assert len(successful_search) > 0
        else:
            return

def testing_merchant_card_yellow_widgets():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.qa_web_link + "/search/si/1/Restaurants/Montreal+QC")
    merchant_card_yellow_widgets()
    print('----------')
    My.search_merchant_page(driver, My.qa_fr_web_link + "/search/si/1/Restaurants/Montreal+QC")
    merchant_card_yellow_widgets()
    driver.quit()
