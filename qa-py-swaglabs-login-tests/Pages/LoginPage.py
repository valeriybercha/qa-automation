from Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.input_login_username_id = Locators.input_login_username_id
        self.input_login_password_id = Locators.input_login_password_id
        self.input_login_submit_xpath = Locators.input_login_submit_xpath
        self.button_error_xpath = Locators.button_error_xpath

    def username_input(self, username):
        self.driver.find_element_by_id(self.input_login_username_id).send_keys(username)

    def password_input(self, password):
        self.driver.find_element_by_id(self.input_login_password_id).send_keys(password)

    def submit_click(self):
        self.driver.find_element_by_xpath(self.input_login_submit_xpath).click()

    def error_button(self):
        self.driver.find_element_by_xpath(self.button_error_xpath)
