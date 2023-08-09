import datetime as dt
import os
import random
import smtplib

import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")


def send_email(subject: str, message: str, recipient: str, smtp_server: str = "smtp.gmail.com", port: int = 587):
    """
    Sends an email using the provided details.

    Parameters:
        - subject: Subject of the email.
        - message: The main content/message of the email.
        - recipient: Email address of the recipient.
        - smtp_server: SMTP server to use for sending the email (default is Gmail's SMTP server).
        - port: Port number to use for the SMTP connection (default is 587 for Gmail).
    """
    MY_EMAIL = os.getenv("MY_EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    with smtplib.SMTP(smtp_server, port) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient, msg=f"Subject:{subject}\\n\\n{message}")


def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it.

    Parameters:
        - file_path: Path to the file to be read.

    Returns:
        - Content of the file as a string.
    """
    with open(file_path, "r") as file:
        return file.read()


def send_birthday_email():
    """
    Sends a birthday email to users whose birthday matches the current date.
    """
    birthdays = pd.read_csv("birthdays.csv")
    letter_templates = [
        "letter_templates/letter_1.txt",
        "letter_templates/letter_2.txt",
        "letter_templates/letter_3.txt"
    ]

    today = dt.datetime.now()
    for _, row in birthdays.iterrows():
        if row["month"] == today.month and row["day"] == today.day:
            letter = read_file(random.choice(letter_templates)).replace("[NAME]", row["name"])
            send_email("Happy Birthday", letter, row['email'])


def send_weekly_quote():
    """
    Sends a motivational quote email if today is Monday.
    """
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == 2:
        quotes = read_file("quotes.txt").split("\n")
        random_quote = random.choice(quotes)
        send_email("Motivational Quote", random_quote, "j@jasonbreedlove.com")


def main(action: str):
    '''
    Main function to determine which email to send based on the provided action.

    Parameters:
        - action: The type of email to send. Accepted values are 'birthday' or 'quote'.
    '''
    if action == "birthday":
        send_birthday_email()
    elif action == "quote":
        send_weekly_quote()
    else:
        print(f"Unknown action: {action}. Accepted values are 'birthday' or 'quote'.")


if __name__ == "__main__":
    # For demonstration purposes, we'll default to sending the weekly quote.
    # In a real-world scenario, you can fetch this value from command-line arguments or other criteria.
    main("quote")
