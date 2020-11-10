import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_01_searching_in_goolge(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("python")
        elem.send_keys(Keys.RETURN)
        assert "www.python.org" in self.driver.page_source
        time.sleep(1)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()