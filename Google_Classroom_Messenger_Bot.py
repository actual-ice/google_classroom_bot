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

cookies = {}
try:
    # Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
    # If it fails, never mind, we'll just login again
    pass


client = Client('iceicebabybabybot@gmail.com', 'i dont think so', session_cookies=cookies)

#Save the session cookies (DO NOT LEAK OR TELL ENYONE ABOUT THE FORBIDDEN CHOCOLATE CHIP COOKIES)
with open('session.json', 'w') as f:
    json.dump(client.getSession(), f)
imap_host = 'imap.gmail.com'
imap_user = 'penullar.isaiah@gmail.com'


# init imap connection
mail = imaplib.IMAP4_SSL(imap_host, 993)
rc, resp = mail.login(imap_user, getpass.getpass())
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
                    if line not in r"Hi Isaiah, If you don't want to receive emails from Classroom, you can unsubscribe  <https://classroom.google.com/s>. Google LLC 1600 Amphitheatre Pkwy Mountain View, CA 94043 USA":
                        message += line + '\n'
        print(message)
        client.send(Message(text=message), thread_id='100001696207106', thread_type=ThreadType.USER)
        
        print("\n----- MESSAGE END -----\n")
        print(str(email_msg['From']))
