import pychrome
from time import sleep

# Define a flag to indicate whether the page has loaded
page_loaded = False

# Define a callback function to handle the load event
def load_event_handler(**kwargs):
    global page_loaded
    page_loaded = True

# Create a new browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# Create a new tab
tab = browser.new_tab()

# Start the tab
tab.start()

# Enable required domains
tab.call_method("Page.enable")
tab.call_method("Runtime.enable")

# Subscribe to the load event
tab.set_listener("Page.loadEventFired", load_event_handler)

# Navigate to the specified URL
tab.call_method("Page.navigate", url="https://music.youtube.com/library/songs")

# Wait for the page to load
while not page_loaded:
    pass

# Execute JavaScript code to click on the element with id "play-button" inside the last child element
click_play_button_script = """
    var parentElement = document.querySelector('#contents > ytmusic-responsive-list-item-renderer:nth-child(14)');
    if (parentElement) {
        var playButton = parentElement.querySelector('#play-button');
        if (playButton) {
            playButton.click();
        }
    }
"""
tab.call_method("Runtime.evaluate", expression=click_play_button_script)

# Wait for a brief moment for the next page to load
sleep(1)

# Execute JavaScript code to click on the element with id "play-button" inside the last child element on the new page
click_play_button_script = """
    var lastChildElement = document.querySelector('#contents > ytmusic-player-queue-item:last-child');
    if (lastChildElement) {
        var playButton = lastChildElement.querySelector('#play-button');
        if (playButton) {
            playButton.click();
        }
    }
"""
tab.call_method("Runtime.evaluate", expression=click_play_button_script)

# Don't close the tab or browser
