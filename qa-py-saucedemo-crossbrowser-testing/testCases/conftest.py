from selenium import webdriver
import pytest

# Configuration file

# Browsers setup
@pytest.fixture()
def setup(browser):

    # Testing in the 'Chrome' browser
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=r'D:/Programming/QA/Projects/qa-automation/qa-py-saucedemo-crossbrowser-testing/Drivers/chromedriver.exe')
        print("Launching Chrome browser.....")

    # Testing in the 'Firefox' browser
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=r'D:/Programming/QA/Projects/qa-automation/qa-py-saucedemo-crossbrowser-testing/Drivers/geckodriver.exe')
        print("Launching Firefox browser.....")

    # Testing in the 'Internet Explorer' browser
    elif browser == "ie":
        driver = webdriver.Ie(executable_path=r'D:/Programming/QA/Projects/qa-automation/qa-py-saucedemo-crossbrowser-testing/Drivers/IEDriverServer.exe')
        print("Launching Internet Explorer browser.....")

    # Testing in the 'Microsoft Edge' browser
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=r'D:/Programming/QA/Projects/qa-automation/qa-py-saucedemo-crossbrowser-testing/Drivers/msedgedriver.exe')
        print("Launching Microsoft Edge browser.....")

    # Testing in the browser by default (Chrome browser)
    else:
        driver = webdriver.Chrome(executable_path=r'D:/Programming/QA/Projects/qa-automation/qa-py-saucedemo-crossbrowser-testing/Drivers/chromedriver.exe')
        print("Launching the default Chrome browser.....")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Setup for the HTML reports generating
def pytest_configure(config):
    config._metadata['Project Name'] = 'Swag Labs'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester Name'] = 'Valeriy B.'
