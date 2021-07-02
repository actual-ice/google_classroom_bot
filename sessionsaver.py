import json
import fbchat

import fbchat # type: ignore
### see https://github.com/fbchat-dev/fbchat/issues/615#issuecomment-710127001 
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

cookies = {}
try:
# Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
#     # If it fails, never mind, we'll just login again
    pass

# Attempt a login with the session, and if it fails, just use the email & password
client = fbchat.Client('iceicebabybabybot@gmail.com', 'XxFreezingIcexX10', session_cookies=cookies, user_agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51')

# ... Do stuff with the client here

# Save the session again
with open('session.json', 'w') as f:
    json.dump(client.getSession(), f)