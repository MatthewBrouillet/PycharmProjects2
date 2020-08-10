import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

global unsubscribe_message_EN
unsubscribe_message_EN = "By submitting this form, you will no longer receive confirmation messages from " \
                         "Yellow Pages Canada regarding submitted rating and reviews."

unsubscribe_message_FR = "En envoyant cette demande, vous cesserez de recevoir des messages de confirmation " \
                                  "de Pages Jaunes Canada concernant les évaluations et les commentaires que " \
                                  "vous avez soumis."


class YPUnsubscribe:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success_EN = False
    is_success_FR = False

    def unsubscribe(self, link):
        """
        >> This function verifies if the appropriate message is displayed
        >> when redirected to the page to unsubscribe
        """
        # Locating the displayed text
        displayed_text = My.search_visibility_webelement(driver, By.TAG_NAME, "h3")

        # Validate the unsubscribe message
        if link[0:26] == My.yp_web_link:
            if displayed_text and displayed_text.text == unsubscribe_message_EN:
                YPUnsubscribe.is_success_EN = True
                return
            else:
                return
        else:
            if displayed_text and displayed_text.text == unsubscribe_message_FR:
                YPUnsubscribe.is_success_FR = True
                return
            else:
                return

    def testing_unsubscribe(self, link):
        """
        >> This function executes the steps of the test case
        """
        My.search_merchant_page(driver, link)
        test.unsubscribe(link)
        if link[0:26] == My.yp_web_link:
            if YPUnsubscribe.is_success_EN:
                print("--> Test case is successful.")
            else:
                print("--> Test case is unsuccessful.")
        else:
            if YPUnsubscribe.is_success_FR:
                print("--> Test case is successful.")
            else:
                print("--> Test case is unsuccessful.")


test = YPUnsubscribe(driver)
test.testing_unsubscribe(
    My.yp_web_link + "/unsubscribeReviewNotification?mid=2735583&merchantEmail=rita.elsalfiti@pj.ca&verificationCode="
                     "e4d16df8-ba85-4386-8847-ed757e83fb35")
print('----------')
test.testing_unsubscribe(
    My.pj_web_link + "/unsubscribeReviewNotification?mid=2735583&merchantEmail=rita.elsalfiti@pj.ca"
                     "&verificationCode=e4d16df8-ba85-4386-8847-ed757e83fb35")
driver.quit()
sys.exit()
