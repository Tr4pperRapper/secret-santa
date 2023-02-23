import random
import smtplib
import pwinput

# Import names and emails from file
with open("names_and_emails.txt") as file:
    # Create an empty list
    namesAndEmails = []

    for line in file:
        # Split the line on whitespace
        lineElements = line.strip().split()

        # Check if the line has at least three elements
        if len(lineElements) >= 3:
	    # Add a tuple with all elements to the list
            namesAndEmails.append((lineElements[0], lineElements[1], lineElements[2]))

# Initialize directory
secretSantaMap = {}

# Randomize names and emails
random.shuffle(namesAndEmails)

# Add entries to the dictionary
for i in range(len(namesAndEmails)):
    secretSantaMap[namesAndEmails[i][2]] = (namesAndEmails[(i+1) % len(namesAndEmails)][0], namesAndEmails[(i+1) % len(namesAndEmails)][1])

# Print pairs
for email, (firstname , lastname) in secretSantaMap.items():
    # Concatenate the last name of the person being paired with their email address
    # Print the email address with the pair's last name alongside their first and last names. 
    print(f'{email}  -> {firstname} {lastname}')

# Get user's email and password
email = input('Email: ')
password = pwinput.pwinput(prompt='Password: ')
print(email)
print(password)
# Confirm action
if input('Do you want to continue and send the emails? (y/n) ').lower() == 'y':
    # Configure Gmail SMTP server
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587

    # Create SMTP object
    smtpObj = smtplib.SMTP(smtpServer, smtpPort)

    # Start SMTP session
    smtpObj.ehlo()

    # Enable TLS encryption
    smtpObj.starttls()

    # Login to Gmail SMTP server
    smtpObj.login(email, password)

    # Loop over entries in dictionary and send emails
    for recipient, (firstname , lastname) in secret_santa_map.items():
        # Configure email message
        message = f'Subject: Secret Santa\n\n You\'re {firstname} {lastname} \'s secret santa. Good luck!'
        # Send email
        smtp_obj.sendmail(email, recipient, message)

    # End SMTP session
    smtpObj.quit()
