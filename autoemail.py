import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up SMTP server credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'Your Email'
SMTP_PASSWORD = 'Password'

# Read in CSV file containing recipient information
recipients_df = pd.read_csv('D:\Code\Automate email\mails.csv')

# Read in email body from a text file
with open('D:\Code\Automate email\email_body.txt', 'r') as f:
    email_body = f.read()

# Loop through each recipient and send an email
for index, recipient in recipients_df.iterrows():
    # Set up email content
    message = MIMEMultipart()
    message['Subject'] = 'Your email subject'
    message['From'] = SMTP_USERNAME
    message['To'] = recipient['email']
    body = email_body.replace('{name}', recipient['name'])
    message.attach(MIMEText(body, 'plain'))

    # Set up SMTP connection and send email
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()
    smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtp_server.sendmail(SMTP_USERNAME, recipient['email'], message.as_string())
    smtp_server.quit()

    print(f"Email sent to {recipient['name']} ({recipient['email']})")
