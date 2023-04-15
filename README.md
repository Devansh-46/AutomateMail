# AutomateMail
This is a Python script that automates the process of sending personalized emails to a list of recipients. The script reads recipient information (names and email addresses) from a CSV file, and uses a text file to specify the body of the email. The script then sends the email to each recipient using the Simple Mail Transfer Protocol (SMTP).

Getting Started
Prerequisites
To run this script, you'll need the following installed on your machine:

Python 3.x
pandas library
smtplib library
Installation
To install the required libraries, you can use pip:


pip install pandas

pip install secure-smtplib

Usage
To use the script, follow these steps:

Clone the repository to your local machine.
Open a terminal and navigate to the project directory.
Create a CSV file with the recipient information. The file should have two columns: "name" and "email". See recipients.csv for an example.
Create a text file with the email body. Use {name} as a placeholder for the recipient's name. See email_body.txt for an example.
Update the SMTP server, port, username, and password in the script with your own information.
Update the file paths for the CSV file and email body in the script, if necessary.
Run the script using the following command: python automated_email_sender.py
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This script was inspired by this tutorial. Thanks to the author for providing a great resource!





