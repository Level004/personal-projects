import pyautogui
import webbrowser

# sets up the browser path and sets the url to the music player
urL = 'https://music.youtube.com/library/songs'
chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))

# opens up chrome and goes to the url
webbrowser.get('chrome').open_new_tab(urL)
pyautogui.sleep(4)

# clicks on the top library track
pyautogui.click(197, 339)

# this has to be done because YT music doesn't use all the tracks in the library
# moves to the bottom of the list and makes sure that every song is loaded
pyautogui.moveTo(1255, 942)
pyautogui.sleep(3)
pyautogui.scroll(-2000)
pyautogui.click()
pyautogui.sleep(3)
pyautogui.scroll(-4000)
pyautogui.click()

# goes to the other playlist and adds it to the queque.
pyautogui.sleep(1)
pyautogui.hotkey('q')
pyautogui.sleep(1)
pyautogui.click(290, 195)
pyautogui.sleep(2)
pyautogui.rightClick(405, 414)
pyautogui.sleep(0.5)
pyautogui.click(490, 592)
pyautogui.hotkey('q')
pyautogui.sleep(0.5)
pyautogui.hotkey('s')
