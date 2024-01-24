import base64
from init.settings import session, GmailAdress
import smtplib
from email.mime.text import MIMEText
import hashlib

with open("../fastApiProject1/templates/img_1.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')


def hashing(data):
    if data:
        return hashlib.sha256(data.encode()).hexdigest()


def photo_changes(user):
    user.photo1 = base64.b64encode(user.photo1).decode('utf-8') if user.photo1 else encoded_string
    user.photo2 = base64.b64encode(user.photo2).decode('utf-8') if user.photo2 else encoded_string


def error_parsing(e):
    session.rollback()
    return f"An error occurred {e}. Please try again."


def send_email(body: str, recipients):
    msg = MIMEText(body)
    msg['Subject'] = 'Album registration'
    msg['From'] = GmailAdress
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login("dhcomsup@gmail.com", "wbfe kfzt ietr lmmi")
        smtp_server.sendmail("dhcomsup@gmail.com", recipients, msg.as_string())  # Use the 'recipients' directly


def creating_cookies(user, status, classroom):
    return {"email": user,
            "user_status": status,
            "classroom": classroom}
