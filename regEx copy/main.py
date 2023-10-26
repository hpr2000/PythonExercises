import re

email_format = r"^[a-zA-Z0-9-._+%]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"


def check_email():
    emails = []
    while True:
        email = input('Enter email or write quit to exit: ')
        if email.lower() == 'quit':
            break

        emails.append(email)

    for email in emails:
        if re.match(email_format, email):
            print(f'{email} is valid.')
        else:
            print(f'{email} is invalid.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_email()
