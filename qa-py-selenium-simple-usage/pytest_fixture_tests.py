# Installing 'pytest' module: pip install pytest
# Test run command: 'pytest <file name>' to run the pytest test in terminal

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
    elif request.param == "edge":
        web_driver = webdriver.Edge()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
    elif request.param == "ie":
        web_driver = webdriver.Ie()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicFFTest:
    pass


class TestPytestFF(BasicFFTest):

    def test_01_python_search(self):
        self.driver.get("https://www.duckduckgo.com")
        assert "DuckDuckGo" in self.driver.title


        # Test without creating a variable
        self.driver.find_element_by_name("q").clear()
        self.driver.find_element_by_name("q").send_keys("python")
        self.driver.find_element_by_name("q").send_keys(Keys.RETURN)
        time.sleep(2)
        assert "www.python.org" in self.driver.page_source

        time.sleep(2)

    def test_02_selenium_search(self):
        self.driver.get("https://www.duckduckgo.com")

        # Test with creating a variable 'selenium_search'
        selenium_search = self.driver.find_element_by_name("q")
        selenium_search.clear()
        selenium_search.send_keys("selenium webdriver")
        selenium_search.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "www.selenium.dev" in self.driver.page_source

        time.sleep(2)