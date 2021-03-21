from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# creating the instance for Chrome Webdriver
driver = webdriver.Chrome()

# If error - Failed to read descriptor from node connection - appeared (uncomment the below lines)
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# maximizing the window
driver.maximize_window()

# navigate to url
driver.get("https://www.ebay.com/")

# verifying webpage title
assert "eBay" in driver.title

# locating a web element by id and sending keys
search = driver.find_element_by_id("gh-ac")
search.clear()
search.send_keys("casio g-shock")
search.send_keys(Keys.RETURN)

# creating 'expected' and 'actual' variables
expected_text = 'casio g-shock'
actual_text = driver.find_element_by_xpath("//h1[@class='srp-controls__count-heading']//span[contains(text(), 'casio g-shock')]").text

# verifying if expected result equals actual result
assert expected_text == actual_text, f"Error. Expected text - {expected_text}"

# waiting for 2 seconds
time.sleep(2)

# closing browser
driver.close()