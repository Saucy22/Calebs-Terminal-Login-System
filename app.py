#Saucy22 on GitHub
#2025

import os
import time
from datetime import datetime


version = "1.0"

pswd = "changeme"
domain = "domain"


signedin = []
signedintime = []

signedout = []
signedouttime = []

print("Welcome to Calebs Terminal Login System version: " + version)
time.sleep(5)
os.system("clear")

print("First, what name will you give this terminal")
domain = input()


print("Second, please create a strong password. This will be used to access administrator commands.")

while True:
    try:
        pswd = input()
        os.system("clear")
        break
    except:
        print("Cannot securely clear terminal, exit the application now.")


print("Now entering main program loop. To abort, hit CTRL+C within the next 5 seconds..")
time.sleep(5)
currentlogs = ("Logs " + str(datetime.now()) + ".txt")
open(currentlogs, "w").write("-Start Logs-")
os.system("clear")
while True:
    try:
        print("Welcome to " + domain)
        time.sleep(1)
        print("Use the /help command for a list of commands or you can sign on using /signon and sign off with /signoff")
        cmd = input()
    except:
        print("Invalid input, to exit please use /quit")
        cmd = "0"
    if cmd == "/help":
        try:
            print(
                "Commands: /help, /signon, /signoff, /quit, /clear" +
                " for detailed information about each command, refer to README.txt"
            )
            time.sleep(5)
        except:
            print("Invalid input, to exit please use /quit")
            cmd = "0"

    if cmd == "/quit":
        try:
            print("Password is required to quit this application.")
            print("Please enter the admin password: ")
            apwd = input()
            time.sleep(2)
            if apwd == pswd:
                print("Thank you for using Terminal Login System")
                time.sleep(1)
                os.system("clear")
                open(currentlogs, "a").write("\n" + "-End Logs-")
                break
            else:
                print("Invalid Password")
        except:
            print("Invalid input, to exit please use /quit")
            cmd = "0"

    if cmd == "/signon":
        try:
            os.system("clear")
            print("Please type in your first and last name")
            name = input()
            signontime = datetime.now()
            time.sleep(2)
            open(currentlogs,"a").write(( "\n" + name + " Has signed on at " + str(signontime) + " on " + domain))
            signedin.append(name)
            signedintime.append(signontime)
            print(name , " Has signed on at " , signontime, " on ", domain)
        except:
            print("Invalid input, to exit please use /quit")
            cmd = "0"

    if cmd == "/signoff":
        try:
            os.system("clear")
            print("Please type in your first and last name EXACTLY how it was typed when you signed in. CaSe SeNsItiVe")
            name = input()
            signouttime = datetime.now()
            time.sleep(2)
            open(currentlogs,"a").write(( "\n" + name + " Has signed out at " + str(signouttime) + " on " + domain))
            signedout.append(name)
            signedouttime.append(signouttime)
            print(name , " Has signed out at " , signouttime, " on ", domain)
        except:
            print("Invalid input, to exit please use /quit")
            cmd = "0"

    if cmd == "/clear":
        os.system("clear")













