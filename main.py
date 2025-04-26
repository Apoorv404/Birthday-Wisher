import pandas
import datetime as dt
import smtplib
from random import randint

today = (dt.datetime.now().month, dt.datetime.now().day)
my_email = ""
password = ""

file = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in file.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_path = f"./letter_templates/letter_{randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{birthday_person["email"]}",
                            msg=f"Subject: Happy Birthday\n\n{contents}.")

print("Email sent successfully.")
