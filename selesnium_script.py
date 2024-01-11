from selenium import webdriver
import time

# Set up the Selenium WebDriver (you need to have the corresponding browser driver installed)
driver = webdriver.Chrome()  # You can use other drivers like Firefox or Edge

# Open the HTML file
driver.get("test/index.html")  # Replace with the actual path to your HTML file

# Wait for 3 seconds
time.sleep(3)

# Simulate a click on the document body
body = driver.find_element_by_tag_name('body')
body.click()

# Wait for a while to observe the color change (you might want to adjust the sleep duration)
time.sleep(2)

# Close the browser
driver.quit()
