import imaplib, email, getpass
from email import policy

# The valid email addresses and their respective subjects

imap_host = 'imap.gmail.com'
imap_user = 'penullar.isaiah@gmail.com'

# "init imap connection" psst i don't know what this doessss
mail = imaplib.IMAP4_SSL(imap_host, 993)
rc, resp = mail.login(imap_user, getpass.getpass())





def new_email():
    '''return the email message and whom the message is from'''
    

    message = ''
    # select only unread messages from inbox
    mail.select('Inbox')
    status, data = mail.search(None, '(UNSEEN)')
    

    # for each e-mail messages, print text content
    for num in data[0].split():
        # get a single message and parse it by policy.SMTP (RFC compliant)
        status, data = mail.fetch(num, '(RFC822)')
        email_msg = data[0][1]
        email_msg = email.message_from_bytes(email_msg, policy=policy.SMTP)
        
        print("\n----- MESSAGE START -----\n")

        print("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n" % ( \
            str(email_msg['From']), \
            str(email_msg['To']), \
            str(email_msg['Date']), \
            str(email_msg['Subject'] )))

        # print only message parts that contain text data
        for part in email_msg.walk():
            if part.get_content_type() == "text/plain":
                for line in part.get_content().splitlines():
                    message += line + '\n'
                    if 'OPEN' in line:
                        link = line
        print(message)

        #if the email is from the given valid email addresses, then send the message
        
        print("\n----- MESSAGE END -----\n")
        print(str(email_msg['From']))

        return message, str(email_msg['From']), link





def valid_email(email_address, valid_emails):
    '''return the subject email is from, and if not valid, return False'''
    #if the email is from the given valid email addresses, then send the message
    if email_address in valid_emails:
        return valid_emails[email_address]
    else: 
        return False
