#       >>> Email Simulator <<<         #

# Class to build email objects
class Email(object):

    def __init__(self, email_address, email_title, email_message):
        self.email_address = email_address
        self.email_title = email_title
        self.email_message = email_message
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# List to store email objects
inbox = []

# Function to append email objects into Inbox List
def populate_inbox():
    inbox.append(Email('madelline.miller@gmail.com', 'Song of Achilles',\
                        'really recommend this book'))
    inbox.append(Email('madelline.miller@gmail.com', 'Circe',\
                        'also really recommend this book'))
    inbox.append(Email('jolkien.rolkien.tolkien@gmail.com', 'The Hobbit',\
                        'who doesn\'t like a cosy read'))

# Function to list emails(address and subject lines) using enumerate to number them  
def list_emails():
    for email_number, email in enumerate(inbox):
        print(f"\n{email_number}\tFrom: {email.email_address}\
              \n\tEmail Subject: {email.email_title}\n")

# Function to read a selected email from while loop menu
def read_email(option):
    while True:
        if 0 <= option < len(inbox):
            email = inbox[option]
            print(f'''\n\t\t\t\tFrom: {email.email_address}
                        \tEmail Subject: {email.email_title}
                        \tEmail Contents: {email.email_message}''')
            email.mark_as_read()
            print(f"\nEmail: '{email.email_title}' marked as read")
            break
        else:
            print("Invalid entry")
            continue
# Tells the populate_inbox function to input email samples
populate_inbox()

# Menu for email simulator providing options to user
while True:
    menu_option = int(input('''\n\t\t\tWould you like to:\n
                                1. Read an email
                                2. View unread emails
                                3. Quit application\n
                                Enter selection: '''))
    
    if menu_option == 1:
        list_emails()
        option = int(input("\nWhich email number would you like to view: "))
        read_email(option)
        continue
    elif menu_option == 2:
        unread = [email for email in inbox if not email.has_been_read]
        if unread:
            print("\n\t\t\t\tYou have opted to read your unread emails")
            for option, email in enumerate(unread):
                print(f"\n\t\t\t\tUnread emails:\t\t{email.email_title}")
            while True:
                request = input('''\n\t\t\t\tPress 'Y' when you are ready
                                to go back to the main menu ''').lower()
                if request == 'y':
                    break
                else:
                    print("\n\t\t\t\tInvalid entry")
                    continue
    elif menu_option == 3:
        print("\n\t\t\t\tYou have exited the program")
        break
    else:
        print("\n\t\t\t\tInvalid entry")
        continue
