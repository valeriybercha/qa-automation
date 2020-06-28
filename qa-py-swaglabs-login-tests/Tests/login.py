from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.LoginPage import LoginPage
from Pages.InventoryPage import InventoryPage
from Locators.locators import Locators
import time


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-swaglabs-login-tests/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(Locators.BaseURL + '/index.html')

    # LOGIN TESTS TO PERFORM:
    # 01) Verify that User is able to Login with Valid Credentials
    # 02) Verify that clicking on browser back and forward buttons after successful login should not log out the user
    # 03) Verify that can successful logout from the system
    # 04) Verify that User is not able to Login with invalid Username and invalid Password
    # 05) Verify that User is not able to Login with Valid Username and invalid Password
    # 06) Verify that User is not able to Login with invalid Username and Valid Password
    # 07) Verify that User is not able to Login with blank Username or Password
    # 08) Verify that locked out User is not able to Login into the system
    # 09) Verify that problem User is able to Login into the system
    # 10) Verify that performance glitched User is able to Login into the system

    # Verify that User is able to Login with Valid Credentials
    def test_01_login_with_valid_credentials(self):
        driver = self.driver
        login = LoginPage(driver)
        login.username_input(Locators.user)
        login.password_input(Locators.password)
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.div_product_label_xpath)

    # Verify that clicking on browser back and forward buttons after successful login should not log out the user
    def test_02_browser_click_back_after_login(self):
        driver = self.driver
        driver.back()
        driver.forward()
        assert driver.find_element_by_xpath(Locators.div_product_label_xpath)

    # Verify that can successful logout from the system
    def test_03_successful_logout(self):
        driver = self.driver
        logout = InventoryPage(driver)
        logout.hamburger_menu_click()
        logout.logout_button_click()
        assert not driver.forward()
        assert driver.find_element_by_id(Locators.input_login_username_id)

    # Verify that User is not able to Login with invalid Credentials
    def test_04_login_with_invalid_credentials(self):
        driver = self.driver
        driver.refresh()
        login = LoginPage(driver)
        login.username_input('invalid_username')
        login.password_input('invalid_password')
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.button_error_xpath)

    # Verify that User is not able to Login with valid Username and invalid Password
    def test_05_login_with_invalid_password(self):
        driver = self.driver
        driver.refresh()
        login = LoginPage(driver)
        login.username_input(Locators.user)
        login.password_input('invalid_password')
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.button_error_xpath)

    # Verify that User is not able to Login with invalid Username and valid Password
    def test_06_login_with_invalid_username(self):
        driver = self.driver
        driver.refresh()
        login = LoginPage(driver)
        login.username_input('invalid_username')
        login.password_input(Locators.password)
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.button_error_xpath)

    # Verify that User is not able to Login with blank Username or Password
    def test_07_login_with_empty_credentials(self):
        driver = self.driver
        driver.refresh()
        login = LoginPage(driver)
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.button_error_xpath)

    # Verify that User is not able to Login with blank Username or Password
    def test_08_locked_out_user_login(self):
        driver = self.driver
        driver.refresh()
        login = LoginPage(driver)
        login.username_input(Locators.user_locked_out)
        login.password_input(Locators.password)
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.button_error_xpath)

    # Verify that problem User is able to Login into the system
    def test_09_problem_user_login(self):
        driver = self.driver
        driver.refresh()
        login = LoginPage(driver)
        login.username_input(Locators.user_problem)
        login.password_input(Locators.password)
        login.submit_click()
        assert driver.find_element_by_xpath(Locators.div_product_label_xpath)
        logout = InventoryPage(driver)
        logout.hamburger_menu_click()
        logout.logout_button_click()

    # Verify that performance glitched User is able to Login into the system
    def test_10_performance_glitched_user_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.username_input(Locators.user_performance_glitch)
        login.password_input(Locators.password)
        login.submit_click()
        driver.implicitly_wait(30)
        assert driver.find_element_by_xpath(Locators.div_product_label_xpath)
        logout = InventoryPage(driver)
        logout.hamburger_menu_click()
        logout.logout_button_click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-swaglabs-login-tests/reports'))