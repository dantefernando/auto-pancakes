# Made by Marcus Sorensen and Dante Fernando 2020
# https://github.com/dantefernando
# https://github.com/exec-marcus

import time
import random
from string import ascii_lowercase, ascii_uppercase
from selenium import webdriver  # pip install selenium
from account import username  # I made an account.py file with my discord username and password here.
from account import password


alphabet = list(ascii_lowercase) + list(ascii_uppercase)  # List of Uppercase and Lowercase letters


class DiscordBot:
    def __init__(self, username1, password1):  # Opens Chrome, Logs into Discord and Goes to Selected Channel.
        self.driver = webdriver.Chrome("C:/Users/Fernpe2/Downloads/chromedriver.exe")  # Change to DIR of chromedriver
        self.driver.get(
            "https://discordapp.com/channels/626436080672964628/696087556273733783")  # Change to Discord Channel
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@type=\"email\"]") \
            .send_keys(username1)  # Types in username at login page
        self.driver.find_element_by_xpath("//input[@type=\"password\"]") \
            .send_keys(password1)  # Types in password at login page
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]") \
            .click()  # clicks submit
        time.sleep(10)
        self.run()

    def run(self):  # Creates a random string of Upper and lowercase letters and sends it in Discord.
        while True:
            word = "".join(random.choice(alphabet) for i in range(random.randint(4, 20)))  # Randomly chooses letters.
            word = word + "\n"
            print(f"Sending: {word}...\n")
            self.driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]") \
                .send_keys(word)  # ^^^Change this XPATH to Channel text box that you type in^^^
            time.sleep(10)

if __name__ == "__main__":
    DiscordBot(username, password)
