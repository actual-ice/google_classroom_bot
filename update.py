import imaplib, email, getpass
from email import policy
from fbchat import Client
from fbchat.models import *
import json

'''THE MAGIC CODE I COPIED THAT MAKES THE CODE WORK LMAOOOOOOOO'''
import fbchat # type: ignore
### see https://github.com/fbchat-dev/fbchat/issues/615#issuecomment-710127001 
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
''''''

# The valid email addresses and their respective subjects
valid_email = {
    '"Divina Gracia Gabute (Classroom)" <no-reply+85708bec@classroom.google.com>':'ESP',
    '"Irene Joy Miranda (Classroom)" <no-reply+52a8659b@classroom.google.com> ':'Science/Homeroom',
    '"Donnabelle Banzon (Classroom)" <no-reply+7e62e0db@classroom.google.com>':'Scientific Writing',
    '"Joel Viana (Classroom)" <no-reply+3a969b59@classroom.google.com>':'MAPEH',
    '"Rolly Bitancor (Classroom)" <no-reply+025c46dc@classroom.google.com>':'MATH',
    '"Mina Lucero (Classroom)" <no-reply+b1609455@classroom.google.com>':'AP',
    '"Eden Paras (Classroom)" <no-reply+986a176c@classroom.google.com>':'AP',
    '"Jayson Zabala (Classroom)" <no-reply+2bc79fdd@classroom.google.com>':'English',
    '"Edna Macauyag (Classroom)" <no-reply+bcf4ffe5@classroom.google.com>':'ICT',
    '"Christine Joy Navidad (Classroom)" <no-reply+6403eff3@classroom.google.com>':'Filipino',
    '"Oliveth Sasha Gliponeo (Classroom)" <no-reply+e715f598@classroom.google.com>':'Research',
    '"Freezing Ice (Classroom)" <no-reply+47717a9e@classroom.google.com>':'Ice'
    }

imap_host = 'imap.gmail.com'
imap_user = 'penullar.isaiah@gmail.com'


# "init imap connection" psst i don't know what this doessss
mail = imaplib.IMAP4_SSL(imap_host, 993)
rc, resp = mail.login(imap_user, getpass.getpass())

cookies = {}
try:
    # Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
    # If it fails, never mind, we'll just login again
    pass

#the client that i don't know how works
client = Client('iceicebabybabybot@gmail.com', 'XxFreezingIcexX10', session_cookies=cookies)

#Save the session cookies (DO NOT LEAK OR TELL ENYONE ABOUT THE FORBIDDEN CHOCOLATE CHIP COOKIES)
with open('session.json', 'w') as f:
    json.dump(client.getSession(), f)
# Check the inbox all the time
while True:
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
        print(message)

        #if the email is from the given valid email addresses, then send the message
        if str(email_msg['From']) in valid_email:
            client.send(Message(text='New announcement in {}'.format(valid_email[str(email_msg['From'])])), thread_id='100001696207106', thread_type=ThreadType.USER)
            # client.send(Message(text='New announcement in {}'.format(valid_email[str(email_msg['From'])])), thread_id='3131183776947815', thread_type=ThreadType.GROUP)
        print("\n----- MESSAGE END -----\n")
        print(str(email_msg['From']))

#somewhat useless maybe idk
