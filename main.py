import os
import smtplib
from dotenv import load_dotenv, dotenv_values
import datetime
import pandas as pd
import random

load_dotenv()

smtp_host = os.getenv("SMTP_HOST")
smtp_port = int(os.getenv("SMTP_PORT"))
smtp_pass = os.getenv("SMTP_PASSWORD")
smtp_email = os.getenv("SMTP_EMAIL")
to_addr = "alicedias2002@hotmail.com"

dir_path = os.path.dirname(os.path.realpath(__file__)) # Get the directory of the current script
current_weekday = datetime.datetime.today().weekday() # Get the current weekday

def read_txt_to_list(file_path):
    """
    Read a text file and return its contents as a list.
    :param file_path: filepath to the text file
    :return: list of strings
    """
    try:
        df = pd.read_csv(file_path, header=None, names=["value"]) # Read the file into a DataFrame
        return df["value"].tolist()  # Return the contents of the file as a list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
def send_email():
    """Send an email using the SMTP server."""
    with smtplib.SMTP(smtp_host, smtp_port) as conn: # Create an SMTP connection
        conn.starttls() # Enable TLS encryption
        conn.login(user=smtp_email, password=smtp_pass) # Log in to the SMTP server
        conn.sendmail(from_addr=smtp_email, to_addrs=to_addr, msg=msg) # Send the email

if current_weekday == 1: # If it's Monday
    quotes = read_txt_to_list(dir_path + "/data/quotes.txt") # Read the quotes from the text file
    quote = random.choice(quotes) # Choose a random quote
    msg = f"Subject: Weekly Motivation\r\n\r\n{quote}" # Create the email message
    send_email() # Call the send_email function

else:
    print("It's not Monday, so no motivation for you today.")