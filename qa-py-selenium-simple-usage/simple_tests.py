# Importing the webdriver and keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Creating the instance of the Chrome driver
driver = webdriver.Chrome()

# Maximizing the window (optional)
driver.maximize_window()

# Navigating to the specified URL
driver.get("https://www.google.com")

# Verifying if 'Google' word is in page title
assert "Google" in driver.title

# Initializing a variable 'elem' and searching for the page element 'q'
elem = driver.find_element_by_name("q")
elem.clear()

# Sending 'python' word to the 'q' input field
elem.send_keys("python")
elem.send_keys(Keys.RETURN)

# Verifying that 'www.python.org' link is displayed on the page
assert "www.python.org" in driver.page_source
time.sleep(2)
driver.close()