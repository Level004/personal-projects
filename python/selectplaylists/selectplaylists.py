import pyautogui
import webbrowser

# sets up the browser path and sets the url to the music player
urL = 'https://music.youtube.com/listen_again'
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# opens up chrome and goes to the url
webbrowser.get('chrome').open_new_tab(urL)



print(pyautogui.position())
