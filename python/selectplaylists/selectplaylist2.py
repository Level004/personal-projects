from playwright.sync_api import sync_playwright

# Initialize Playwright
with sync_playwright() as p:
    # Connect to the existing Chrome browser instance with remote debugging enabled
    browser = p.chromium.connect_over_cdp(endpoint_url="http://localhost:9222")

    # Open a new tab in the existing browser instance
    context = browser.new_context()
    page = context.new_page()

    # Perform tasks in the new tab
    page.goto('https://www.google.com')

    # Keep the tab open for demonstration purposes
    input("Press Enter to close the tab...")

    # Close the context (tab)
    context.close()

    # Note: The existing browser instance remains open unless explicitly closed
