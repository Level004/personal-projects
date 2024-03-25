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
    var retryInterval = setInterval(function() {
    var parentElement = document.querySelector('#contents > ytmusic-responsive-list-item-renderer:nth-child(14)');
    if (parentElement) {
        console.log('Parent element found');
        clearInterval(retryInterval);
        var playButton = parentElement.querySelector('#play-button');
        if (playButton) {
            console.log('Play button found');
            var initialUrl = window.location.href;
            playButton.click();

            var intervalID = setInterval(function() {
                console.log('Checking if URL changes');
                if (initialUrl !== window.location.href) {
                    console.log('URL changed, stopping interval');
                    clearInterval(intervalID);
                } else {
                    console.log('URL did not change, clicking again');
                    playButton.click();
                }
            }, 1000);
        } else {
            console.log('Play button not found');
        }
    } else {
        console.log('Parent element not found');
    }
}, 1000);
"""
tab.call_method("Runtime.evaluate", expression=click_play_button_script)

# Execute JavaScript code with integrated interval
add_playlist_to_queue = """
    var retryInterval = setInterval(function() {
    var lastChildElement = document.querySelector('#contents > ytmusic-player-queue-item:last-child');
    if (lastChildElement) {
        console.log('Found last child element');
        clearInterval(retryInterval);
        var playButton = lastChildElement.querySelector('#play-button');
        if (playButton) {
            console.log('Found play button');
            playButton.click();

            var intervalID = setInterval(function() {
                var stopElement = document.querySelector('ytmusic-player-queue[should-hide-auto-play-header] .autoplay.ytmusic-player-queue');
                if (!stopElement) {
                    console.log('Stop element not found, stopping interval');
                    clearInterval(intervalID);

                    function clickOnPlaylist() {
                        var guideEntries = document.querySelectorAll('#items > ytmusic-guide-entry-renderer > tp-yt-paper-item');
                        for (var i = 0; i < guideEntries.length; i++) {
                            var ytFormattedString = guideEntries[i].querySelector('yt-formatted-string');
                            if (ytFormattedString && ytFormattedString.textContent.trim() === 'YT music extra') {
                                console.log('yt-formatted-string with correct text found in guide entry ' + i);
                                guideEntries[i].click();
                                console.log('Clicked on guide entry ' + i);
                                break;
                            }
                        }

                        function addToQueue() {
                            console.log("adding to queue")
                            document.querySelector('#button-shape > button > yt-touch-feedback-shape > div').click();
                            setTimeout(() => {
                                document.querySelector('#items > ytmusic-menu-service-item-renderer:nth-child(2)').click();
                            }, 1000);
                        }
                        setTimeout(() => {
                            addToQueue();
                        }, 4000);
                    }
                    clickOnPlaylist();
                } else {
                    console.log('Stop element found, continuing');
                    lastChildElement = document.querySelector('#contents > ytmusic-player-queue-item:last-child');
                    playButton = lastChildElement.querySelector('#play-button');
                    playButton.click();
                }
            }, 1000);
        } else {
            console.log('Play button not found');
        }
    } else {
        console.log('Last child element not found');
    }
}, 1000);
"""
sleep(3)
tab.call_method("Runtime.evaluate", expression=add_playlist_to_queue)

