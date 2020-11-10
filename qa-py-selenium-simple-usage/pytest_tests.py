# Installing 'pytest' module: pip install pytest
# Test run command: 'pytest <file name>' to run the pytest test in terminal

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestPytest:

    def test_01_google_search_python(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title


        # Test without creating a variable
        self.driver.find_element_by_name("q").clear()
        self.driver.find_element_by_name("q").send_keys("python")
        self.driver.find_element_by_name("q").send_keys(Keys.RETURN)
        assert "www.python.org" in self.driver.page_source

        time.sleep(2)
        self.driver.close()

    def test_02_google_search_selenium(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get("https://www.google.com")

        # Test with creating a variable 'selenium_search'
        selenium_search = self.driver.find_element_by_name("q")
        selenium_search.clear()
        selenium_search.send_keys("selenium")
        selenium_search.send_keys(Keys.RETURN)
        assert "Selenium Webdriver" in self.driver.page_source

        time.sleep(2)
        self.driver.close()
        self.driver.quit()




