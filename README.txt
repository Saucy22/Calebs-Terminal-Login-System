Caleb's Terminal Login System (CTLS)
Documentation

0. Credits:
Saucy22 on Github

1. Setup:
In order to use this program you must:
    -Have python3 installed.
    -Be in a linux shell
To run this program simply change directories into the folder its in and run the command:
    "python3 app.py"
After running this program you will be required to name the terminal and give it a password. Follow the instructions on screen.
Before entering the main program loop you have a chance to abort the program by using CTRL+C, you must do this before 5 seconds runs out.
After entering the main program loop you must quit using the "/quit" command. You will need the admin password (that you made during setup) to do this.

2. Commands:

"/help":
Displays a list of all available commands. Can be done by any user

"/clear":
Clears the terminal and displays the welcome message again. Can be done by any user

"/signon":
Prompts the user to sign on, user must enter his/her name into the terminal. The date and time this is done on is saved to logs, along with the name that the user put in. Can be done by any user.

"/signoff":
Prompts the user to sign off, user must enter his/her name into the terminal. The date and time this is done on is saved to logs, along with the name that the user put in. Can be done by any user.

"/quit":
Quits the program and ends the log. Only users with the admin password may do this.
