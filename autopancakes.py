# Made by Marcus Sorensen and Dante Fernando 2020
# https://github.com/dantefernando
# https://github.com/exec-marcus

import time
import random
from string import ascii_lowercase, ascii_uppercase
from selenium import webdriver  # pip install selenium
from account import username  # I made an account.py file with my discord username and password here.
from account import password
from datetime import datetime


alphabet = list(ascii_lowercase) + list(ascii_uppercase)  # List of Uppercase and Lowercase letters


class DiscordBot:
    def __init__(self, username1, password1):  # Opens Chrome, Logs into Discord and Goes to Selected Channel.
        self.driver = webdriver.Chrome("C:/Users/Fernpe2/Downloads/chromedriver.exe")  # Change to DIR of chromedriver
        time_now = self.findtime()
        print(f"[{time_now}] Opening Chrome...\n")
        self.driver.get(
            "https://discordapp.com/channels/626436080672964628/696145489997070367")  # Change to Discord Channel
        time.sleep(5)
        time_now = self.findtime()
        print(f"[{time_now}] Entering Account Details...\n")
        self.driver.find_element_by_xpath("//input[@type=\"email\"]") \
            .send_keys(username1)  # Types in username at login page
        self.driver.find_element_by_xpath("//input[@type=\"password\"]") \
            .send_keys(password1)  # Types in password at login page
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]") \
            .click()  # clicks submit
        time_now = self.findtime()
        print(f"[{time_now}] Successfully Logged into Discord!\n")
        print("#############################\n")
        time.sleep(10)
        self.run()

    def run(self):  # Creates a random string of Upper and lowercase letters and sends it in Discord.
        while True:
            time_now = self.findtime()
            word = "".join(random.choice(alphabet) for i in range(random.randint(4, 20)))  # Randomly chooses letters.
            word = word + "\n"
            print(f"[{time_now}] Sending: {word.rstrip()}...\n")
            self.driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]") \
                .send_keys(word)  # ^^^Change this XPATH to Channel text box that you type in^^^
            time.sleep(10)

    def findtime(self):  # Gets current Time for logging.
        d = datetime.now()  # Gets current time
        hour = d.hour  # Gets hour
        minute = d.minute  # Gets minute
        second = d.second  # Gets second
        if minute <= 9:  # Adds 0 to start of string if the minute is less than 10 (Just to make time look normal)
            minute = str(minute)
            minute = "0" + minute
        else:
            pass
        if second <= 9:  # Adds 0 to start of string if the second is less than 10 (Just to make time look normal)
            second = str(second)
            second = "0" + second
        else:
            pass

        time_now = f"{hour}:{minute}:{second}"  # Formats time
        return time_now  # Returns time


if __name__ == "__main__":
    DiscordBot(username, password)
