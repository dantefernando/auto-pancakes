# Script made by Dante Fernando 2020
# https://github.com/dantefernando/auto-pancakes

# Original Idea by Marcus Sorensen 2020
# https://github.com/exec-marcus/randomideas/blob/master/pancakey2

import time
import random
from string import ascii_lowercase, ascii_uppercase
from selenium import webdriver  # pip install selenium
from account import username, password  # I made an account.py file with my discord username and password here.
from datetime import datetime, timedelta

alphabet = list(ascii_lowercase) + list(ascii_uppercase)


def open_discord(username1, password1, driver):  # Opens Chrome, Logs into Discord and Goes to Selected Channel.
    get_log("Opening Discord...")
    driver.get(
        "https://discordapp.com/channels/626436080672964628/696145489997070367")  # Change to Discord Channel
    time.sleep(5)
    get_log(f"Logging into account: {username1} ...")
    driver.find_element_by_xpath("//input[@type=\"email\"]") \
        .send_keys(username1)  # Types in username at login page
    driver.find_element_by_xpath("//input[@type=\"password\"]") \
        .send_keys(password1)  # Types in password at login page
    driver.find_element_by_xpath("//button[@type=\"submit\"]") \
        .click()  # clicks submit
    get_log("Successfully logged into Discord!")
    print("#############################\n")
    time.sleep(10)


def send_word(driver):  # Creates a random string of Upper and lowercase letters and sends it in Discord.
    while True:
        for i in range(6):  # Repeats 12 times (2 Minutes Total Cooldown before checking file)
            word = "".join(random.choice(alphabet) for i in range(random.randint(4, 20)))  # Randomly chooses letters.
            word = word + "\n"
            get_log(f"Sending: {word.rstrip()}...")
            driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]"
                "/div[2]") \
                .send_keys(word)  # ^^^Change this XPATH to Channel text box that you type in^^^
            time.sleep(10)
        write_daily = checkfile(driver)  # "write_daily = True": Been more than 24 hours since last !p daily
        if write_daily:
            word = "!p daily" + "\n"
            get_log(f"Sending: {word.rstrip()}...")
            driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div["
                "3]/div[2]") \
                .send_keys(word)  # ^^^Change this XPATH to Channel text box that you type in^^^
            time.sleep(10)
        else:
            pass


def get_log(task):  # Gets current Time for logging.
    d = datetime.now()
    hour, minute, second = d.hour, d.minute, d.second
    if minute <= 9:  # Adds 0 to start of string if the minute is less than 10 (Just to make time look normal)
        minute = "0" + str(minute)
    else:
        pass
    if second <= 9:  # Adds 0 to start of string if the second is less than 10 (Just to make time look normal)
        second = "0" + str(second)
    else:
        pass
    time_now = f"{hour}:{minute}:{second}"
    print(f"[{time_now}] {task}\n")


def setupdaily(driver):  # Sends first !p daily when running the program for the first time
    word = "!p daily" + "\n"
    get_log(f"Sending SETUP: {word.rstrip()}...")
    driver.find_element_by_xpath(
        "/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div["
        "3]/div[2]") \
        .send_keys(word)  # ^^^Change this XPATH to Channel text box that you type in^^^
    time.sleep(10)


def comparetimes(last_full):
    d_last_year = int(last_full[0:4])
    d_last_month = int(last_full[5:7])
    d_last_day = int(last_full[8:10])
    d_last_hour = int(last_full[11:13])
    d_last_minute = int(last_full[14:16])
    d_last_second = int(last_full[17:19])
    d_current = datetime.now()
    d_last = d_current.replace(year=d_last_year, month=d_last_month, day=d_last_day, hour=d_last_hour,
                               minute=d_last_minute, second=d_last_second)
    d_24hr = d_last + timedelta(days=1)
    if d_current > d_24hr:
        with open("daily.txt", "w") as file:  # Rewrite file
            file.write(f"{d_current}")  # Record new time for last !p daily sent
            file.close()
            write_daily = True
            return write_daily
    else:
        print("Too Early for your daily, try again!")
        write_daily = False
        return write_daily


def checkfile(driver):
    d = datetime.now()
    try:  # Check for existing file by trying to read the file
        with open("daily.txt", "r") as file:
            whole_file = file.readlines()
            print("Found previous log of daily")
            last_full = whole_file[0]  # Stores first line of daily.txt (E.g. "2020-04-08 21:17:57.306202") as str
            file.close()
            write_daily = comparetimes(last_full)  # Checks if it has been over 24 hours since
            return write_daily

    except IOError:  # If daily.txt is not found, make a new file
        with open("daily.txt", "w") as file:  # Creates the file and adds date
            file.write(f"{d}")
            file.close()
            file = open("daily.txt", "r")
            whole_file = file.readlines()
            last_full = whole_file[0]  # Stores first line of daily.txt (E.g. "2020-04-08 21:17:57.306202") as str
            print("No trace of previous Daily attempt, creating new log.")
            file.close()
            setupdaily(driver)
            write_daily = comparetimes(last_full)  # Checks if it has been over 24 hours
            return write_daily  # since last !p daily


def first_vote():  # First time setup, if user has already redeeemed !p daily, they can configure it through here.
    try:  # Check for existing file by trying to read the file
        with open("daily.txt", "r") as file:
            file.close()
    except IOError:  # If daily.txt is not found, make a new file
        print("\n-------FIRST TIME CONFIGURATION-------\n")
        while True:
            user_input = str(input("Have you redeemed your !p daily today yet? [y/n]\nAnswer: "))
            if user_input.lower() == "yes" or user_input.lower() == "y":
                print("Go to Discord, type \"!p daily\" and check how many hours, minutes and seconds until\n your "
                      "next !p daily. You will need to enter them below to configure the bot for further use...")
                while True:
                    try:
                        d = datetime.now()
                        hours_in = int(input("Hours: "))
                        minutes_in = int(input("Minutes: "))
                        seconds_in = int(input("Seconds: "))
                        next_vote = d + timedelta(hours=hours_in, minutes=minutes_in, seconds=seconds_in)
                        last_vote = next_vote - timedelta(hours=24)
                        with open("daily.txt", "w") as file:  # First time setup, creates the file and adds date
                            file.write(f"{last_vote}")
                            file.close()
                        print("Configuration Complete!!")
                        break
                    except TypeError:
                        print("Invalid Data Type, please use INTEGERS!")
                break
            elif user_input.lower() == "no" or user_input.lower() == "n":
                print("Configuration Complete!!")
                print("\n !! IMPORTANT: You must run the script for at least 1 MINUTE for First Time Configuration \n"
                      "to be completed. !!\n")
                break
            else:
                print("Invalid option try again...")


def main():
    first_vote()  # First time setup, if user has already redeemed their !p daily, they can configure it through here.
    driver = webdriver.Chrome("C:/Users/Fernpe2/Downloads/chromedriver.exe")  # Change to DIR of chromedriver
    open_discord(username, password, driver)
    send_word(driver)


if __name__ == "__main__":
    main()
