# auto-pancakes
## About
A Python script that sends a randomized string of letters into a specific discord channel that tricks Pancake Bot (https://pancake.gg) into thinking you're "active" therefore giving you Pancakes in return. 

## Dependencies
 - **Selenium:** `pip install selenium`
 - **Chrome Webdriver** installed on your computer (https://chromedriver.chromium.org/downloads) *Choose the appropriate download for your chrome version* `chrome://version`
 
 ## Setup
 - Change the username and password variables in "account.py" to your discord email and password for Login
 - Change the Directory of the chromedriver.exe in LINE 18
 - Change the Discord Channel URL to whatever Discord Channel you prefer in LINE 20
 - Change the XPATH of of the Discord text entry box to your preferred channel (Inspect the Text Entry Box > Right Click > Copy> Copy Full XPATH > Paste that into line 37)

#### Changelog
[April 4th 2020]
V.10 Initial Build
