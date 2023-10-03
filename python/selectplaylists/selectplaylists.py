import pyautogui

# clicks on a library track
pyautogui.click(x=362, y=992)

# this has to be done because YT music doesn't use all the tracks in the library
# moves to the bottom of the list and makes sure that every song is loaded
pyautogui.moveTo(x=1337, y=947)
pyautogui.sleep(6)
pyautogui.scroll(-4000)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.sleep(4)
pyautogui.scroll(-4000)
pyautogui.click()

# goes to the other playlist and adds it to the queque.
pyautogui.sleep(4)
pyautogui.click(x=80, y=555)
pyautogui.sleep(4)
pyautogui.click(x=952, y=445)
pyautogui.sleep(0.5)
pyautogui.click(x=1020, y=548)
pyautogui.hotkey('q')
pyautogui.sleep(0.5)
pyautogui.hotkey('s')
pyautogui.hotkey('j')
pyautogui.hotkey('s')
