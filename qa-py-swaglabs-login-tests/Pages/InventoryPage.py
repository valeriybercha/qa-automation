from Locators.locators import Locators


class InventoryPage():

    def __init__(self, driver):
        self.driver = driver
        self.button_hamburger_menu_xpath = Locators.button_hamburger_menu_xpath
        self.a_logout_button_id = Locators.a_logout_button_id

    def hamburger_menu_click(self):
        self.driver.find_element_by_xpath(self.button_hamburger_menu_xpath).click()

    def logout_button_click(self):
        self.driver.find_element_by_id(self.a_logout_button_id).click()
