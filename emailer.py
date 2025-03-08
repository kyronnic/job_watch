import smtplib
from email.message import EmailMessage
from os import getenv
from credentialer import get_api_key

def send_email(message):
    gmail_user = getenv('gmail_user')
    gmail_password = get_api_key()

    msg = EmailMessage()
    msg.set_content(
        message
    )
    msg['Subject'] = 'New Jobs at PlayStation'
    msg['To'] = 'ktcarter1215@icloud.com'
    msg['From'] = gmail_user

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
        print("Sent successfully")
    except:
        print("Failed")

