import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
driver = webdriver.Chrome(My.PATH)

global unsubscribe_message_EN
unsubscribe_message_EN = "By submitting this form, you will no longer receive confirmation messages from " \
                         "Yellow Pages Canada regarding submitted rating and reviews."


def unsubscribe():
    """
    >> This function verifies if the appropriate message is displayed
    >> when redirected to the page to unsubscribe
    """
    # Locating the displayed text
    displayed_text = My.search_visibility_webelement(driver, By.TAG_NAME, "h3")

    # Validate the unsubscribe message
    assert displayed_text and displayed_text.text == unsubscribe_message_EN


def testing_unsubscribe():
    """
    >> This function executes the steps of the test case
    """
    My.search_merchant_page(driver, My.Testing_Env_EN + \
           "/unsubscribeReviewNotification?mid=2735583&merchantEmail=rita.elsalfiti@pj.ca&verification" \
           "Code=e4d16df8-ba85-4386-8847-ed757e83fb35")
    unsubscribe()
    driver.quit()
