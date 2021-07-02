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

#the client that i don't know how works
client = Client('iceicebabybabybot@gmail.com', 'XxFreezingIcexX10', session_cookies=cookies)

#Save the session cookies (DO NOT LEAK OR TELL ENYONE ABOUT THE FORBIDDEN CHOCOLATE CHIP COOKIES)
with open('session.json', 'w') as f:
    json.dump(client.getSession(), f)

def send_message(mail_address):
    client.send(Message(text='New announcement in {}'.format(mail_address)), thread_id='100001696207106', thread_type=ThreadType.USER)
    # client.send(Message(text='New announcement in {}'.format(valid_email[str(email_msg['From'])])), thread_id='3131183776947815', thread_type=ThreadType.GROUP)