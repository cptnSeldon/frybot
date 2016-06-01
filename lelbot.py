"""  """
import time
import json
from random import randrange
from slackclient import SlackClient
import giphypop

"""
http://futurama-quotes.tumblr.com/
https://en.wikiquote.org/wiki/Futurama
"""

# ATTRIBUTES
token = "token"
sc = SlackClient(token)
chan_random = "random"
chan_general = "general"
chan_fry = "fry"
giphy_public_key = "dc6zaTOxFJmzC"
"""
    FRYBOT : class
"""

""" CONNECTION METHODS """
# CONNECTION

# DECONNECTION

""" DETECTION METHODS """
# USER DETECTION

# CHANNEL DETECTION


# KEYWORD DETECTION
def detect_keyword(event):

    # retrieve user info
    user_info = slack_client.api_call('users.info', user=event["user"])
    user_name = user_info['user']['name']
    # actual test
    if event["text"].startswith("fgif"):
        print(slack_client.api_call("chat.postMessage", as_user="true", channel=chan_fry,
                                    text="Shut up and take my Gif!",
                                    attachments=json.dumps([{"title": "image", "image_url": fgif(event).media_url}])))

    elif event["text"].startswith("fquote"):
        print(slack_client.api_call("chat.postMessage", as_user="true", channel=chan_fry,
                                    text="@"+user_name+": "+fquote(event)))

    elif event["text"].startswith("fpict"):
        print(slack_client.api_call("chat.postMessage", as_user="true", channel=chan_fry,
                                    text="@"+user_name+": "+fpict(event)))


""" MAIN METHODS """


# SEND GIF using giphypop
def fgif(parameter):
    query = parameter["text"][5:]
    g = giphypop.Giphy()
    response = g.search_list("Futurama", query)
    index = randrange(0, len(response))
    return response[index]


# SEND PICTURE
def fpict(parameter):
    return "I am a picture " + parameter["text"][6:]


# SEND QUOTE
def fquote(parameter):
    return "I am a quote " + parameter["text"][7:]

#test connection
print(slack_client.api_call("api.test"))
print(slack_client.api_call("im.open"))
print(slack_client.api_call("auth.test"))

if slack_client.rtm_connect():

    print(slack_client.api_call("users.list"))

    while True:

        checkEvent = slack_client.rtm_read()

        for event in checkEvent:
            #print(event)
            if "type" in event:
                if event["type"] == "message" \
                        and "text" in event \
                        and "bot_id" not in event \
                        and event["channel"] == chan_fry:
                    message = event["text"]
                    detect_keyword(event)
        time.sleep(1)
else:
    print("Connection failed")


"""
    MAIN
"""
