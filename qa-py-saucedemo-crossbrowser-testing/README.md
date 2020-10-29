# Crossbrowser testing (Chrome, Firefox, IE, Edge) of login form based on automation framework (POM) using Python, Selenium Webdriver, Pytest.
Automated login tests of SwagLabs demo application (https://www.saucedemo.com) using Selenium Webdriver, Python, Pytest, Pytest-xdist (for running tests in parallel) and Pytest-html (for generating html reports). 

### Usage:

Run tests in terminal: 
```sh
pytest -v -s testCases/<tests file>.py
```
Run tests in different browsers (Chrome, Firefox, IE, Edge):
```sh
pytest -v -s testCases/<tests file>.py --browser <browser name> (chrome, firefox, ie, edge)
```
Run tests in parallel:
```sh
pytest -v -s -n=2 (number of tests to execute in parallel) testCases/<tests file>.py --browser <browser name>
```
Run tests with html-report generating:
```sh
pytest -v -s -n=2 --html=Reports/report.html (command to generate html reports) testCases/<tests file>.py --browser <browser name>
```