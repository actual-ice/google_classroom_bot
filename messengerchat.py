
from fbchat import Client
from fbchat.models import *

cookies = {}
try:
# Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
# If it fails, never mind, we'll just login again
    pass

client = Client("iceice.babybaby.79", "XxFreezingIcexX15", session_cookies=cookies, user_agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36')
session_cookies = client.getSession()
client.setSession(session_cookies)
while True:
    client.send(Message(text="Hi me!"), thread_id='100001696207106', thread_type=ThreadType.USER)
