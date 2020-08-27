import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)


def widgets():
    """
    >> This function verifies the widgets are present on the merchant page.
    """
    driver.implicitly_wait(5)
    # Locating the container
    container = My.search_presence_webelements(
        driver, By.XPATH, "//*[@id='ypgBody']/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li")
    assert container

    # Looping through each widget
    for i in container:
        widget = My.search_clickable_webelement(i, By.TAG_NAME, "a")
        print(widget.text)
        if widget:
            assert widget.text == "Phone Number" or "Reserve" or "Message" \
                   or "Send Message" or "Directions" or widget.text == "Website"


def testing_schnitzel_widgets():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + "/bus/r/Ontario/Toronto/Schnitzel-Hub-European-Bistro/7119328.html")
    widgets()
    driver.quit()
