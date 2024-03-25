# <i>Python projects</i>

# Resin Counter

this script allows you to see how much resin you have in the game Genshin impact

| ENV Value  | Description      |
|------------|------------------|
| LTUID      | The ltuid        |
| LTOKEN     | The ltoken       |
| GENSHINUID | Your genshin UID |

To get the ltuid and the ltoken you need to:

1. go to hoyolab while logged in
2. open up inspect element
3. go to network and reload the page
4. scroll up until you see some that starts with 'postList?id='
5. click on it and then click on 'Cookies'
6. copy both the values of the ltuid and the ltoken into their respective ENV variables


# Select Playlists 
an automated way for me to open up my playlists
### this only works for chrome
if you want to use it for yourself here is how:

1. you have to launch chrome with this flag `chrome.exe --remote-debugging-port=9222`
2. change the playlist name on line 117 to your desired playlist
