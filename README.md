# auto-pancakes
## About
A Python script that sends a randomized string of letters into a specific discord channel that tricks [Pancake Bot](https://pancake.gg) into thinking you're "active" therefore giving you Pancakes in return and automatically gets daily pancakes every 24 hours. Apon running auto-pancakes, a chrome window will open and automatically login, go to the set discord channel and start sending random messages. You can minimize the window after and leave it running in the background.

- Made by [Dante Fernando](https://github.com/dantefernando)
- Original Idea by [Marcus Sorensen](https://github.com/marcus-dk)

## Dependencies
 - **Selenium:** 
 ```
 pip install selenium
 ```
 - **Chrome Webdriver** installed on your computer [Download here](https://chromedriver.chromium.org/downloads) *Choose the appropriate download for your chrome version* 
 ```
 chrome://version
 ```
 
 ## Setup (IMPORTANT)
 - Change the **username** and **password** variables in "account.py" to your **discord email and password** for Login
 - Change the **Directory of the chromedriver.exe** in **LINE 169**
 - Change the **Discord Channel URL** to whatever Discord Channel you prefer in **LINE 20**
 - Change the **XPATH of of the Discord text entry box** for your preferred channel in **LINE 41** *(Code should work without this step)*
 ```
 Open Chrome > Inspect the Text Entry Box > Right Click > Copy > Copy Full XPATH > Paste that into LINE 41
 ```

## Changelog

##### [April 4th 2020]
**v1.0** Initial Build

#### [April 5th 2020]
**v1.1** Added time to logs and made logs look nicer when sending messages to Discord :)

#### [April 13th 2020]
**v2.0** Automatically sends "!p daily" every 24 hours and remembers when your last "!p daily" was sent. You'll never forget to redeem your daily pancakes ever again!
