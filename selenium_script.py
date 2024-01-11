from selenium import webdriver
import time

# Set up the Selenium WebDriver in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

try:
    # Open the HTML page in the browser
    driver.get("/a/index.html")  # Replace with the actual path or URL

    # Wait for the page to load
    time.sleep(3)

    # Simulate a click on the document
    body = driver.find_element_by_tag_name('body')
    body.click()

    # Wait for a while to observe the color change (you might want to adjust the sleep duration)
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
