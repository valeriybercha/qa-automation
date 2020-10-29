import time

# Login page locators


class LoginPage:

    # Login form locators
    input_username_xpath = "//input[@id='user-name']"
    input_password_xpath = "//input[@id='password']"
    button_login_xpath = "//input[@id='login-button']"

    # Products page locators
    button_hamburger_menu_xpath = "//button[contains(text(),'Open Menu')]"
    a_logout_link_xpath = "//a[@id='logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_xpath(self.input_username_xpath).clear()
        self.driver.find_element_by_xpath(self.input_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.input_password_xpath).clear()
        self.driver.find_element_by_xpath(self.input_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.button_hamburger_menu_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.a_logout_link_xpath).click()
