import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email(html, subject, to_email):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = os.getenv('SMTP_USERNAME')
    message['To'] = to_email

    # Attach the HTML content
    message.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
            server.starttls()
            server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
            server.sendmail(message['From'], message['To'], message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
