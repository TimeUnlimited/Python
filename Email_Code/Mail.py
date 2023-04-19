from email.message import EmailMessage
import smtplib
import datetime
import os
import sys
import time

print('''

  ┌────────────────────────────────────┐
  │        Shipping & Receiving        │
  ├────────────────────────────────────┤
  │ Version: 1.1                       │
  │ By: TimeUnlimited                  │
  └────────────────────────────────────┘
         
   ''')

def create_file_if_not_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            if filename == "data.txt":
                file.write("| Part name/number |    Date    |   Status   |\n")
                file.write("-" * 41 + "\n")

def write_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)

def loading_bar():
    sys.stdout.write("Sending email")
    for _ in range(10):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)
    print("\nEmail sent successfully.\n")

def send_email(sender, recipient, body, message):
    try:
        email = EmailMessage()
        email["From"] = sender
        email["To"] = recipient
        email["Subject"] = ("Shipping Update for Part: " + body)
        email.set_content(message)

        with smtplib.SMTP("smtp.office365.com", port=587) as smtp:
            smtp.starttls()
            smtp.login(sender, "password")
            smtp.sendmail(sender, recipient, email.as_string())
            loading_bar()
    except Exception as e:
        with open("error_log.txt", "a") as error_log:
            error_log.write(f"{datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')} - {str(e)}\n")
        print("\nAn error occurred. Check error_log.txt for details.\n")

create_file_if_not_exists("data.txt")
create_file_if_not_exists("suggestions.txt")
create_file_if_not_exists("error_log.txt")

sender = "email"
recipient = "email"

while True:
    option = input('''Please scan the Recieved or Shipped QR code: ''')

    if option == "0":
        print("Exiting program...")
        break

    elif option == "2":
        message = "Part has been shipped"
        status = "shipped"

    elif option == "1":
        message = "Part has been received"
        status = "received"

    elif option == "3":
        suggestion = input('''
      Please make a suggestion as to what you would like to see added!
      User: ''')
        write_to_file("suggestions.txt", f"{datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')} - {suggestion}\n")
        print('''
      Thanks for the suggestion!
      ''')
        continue

    elif option == "4":
        print('''
        Update Log

        3/24/2023: Version 1.1 Progress bar, database, and suggestions box have been added!

        3/22/2023: Version 1.0 The first release of the program has been created!
        ''')
        continue

    else:
        print("Invalid option")
        continue

    body = input('Please enter a part name/number: ')

    send_email(sender, recipient, body, message)

    date = datetime.datetime.now().strftime("%m/%d/%Y")
    formatted_line = "| {body:^18} | {date:^10} | {status:^9} |\n".format(body=body, date=date, status=status)
    write_to_file("data.txt", formatted_line)
