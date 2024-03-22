from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the URL of the Chrome DevTools Protocol server
chrome_devtools_url = "http://localhost:9222"

# Specify the path to the Chrome driver executable
chrome_driver_path = "C:/Users/guill/Documents/chromedriver-win64/chromedriver.exe"

# Create a Chrome service object with the specified URL and executable path
chrome_service = Service(executable_path=chrome_driver_path)

# Connect to the existing Chrome instance using the Chrome service
browser = webdriver.Chrome(service=chrome_service)

# Now you can interact with the browser as needed
browser.get('https://www.google.com')

# Keep the browser open for demonstration purposes
input("Press Enter to close the browser...")

# # Close the browser
# browser.quit()
