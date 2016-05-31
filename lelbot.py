"""  """
import time
from slackclient import SlackClient

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


""" METHODS """
# DETECT KEYWORD


def detect_keyword(event):
    # retrieve user info
    user_info = slack_client.api_call('users.info', user=event["user"])
    user_name = user_info['user']['name']
    print(user_name)
    # actual test
    if event["text"].startswith("fgif"):
        print(slack_client.api_call("chat.postMessage", as_user="true:", channel=chan_fry, text="@"+user_name+": "+fgif(event)))
    elif event["text"].startswith("fquote"):
        print(slack_client.api_call("chat.postMessage", as_user="true:", channel=chan_fry, text="@"+user_name+": "+fquote(event)))
    elif event["text"].startswith("fpict"):
        print(slack_client.api_call("chat.postMessage", as_user="true:", channel=chan_fry, text="@"+user_name+": "+fpict(event)))


# SEND GIF
def fgif(parameter):
    return "I am a gif of " + parameter["text"][4:]


# SEND PICTURE
def fpict(parameter):
    return "I am a picture " + parameter["text"][5:]


# SEND QUOTE
def fquote(parameter):
    return "I am a quote " + parameter["text"][5:]

#test connection
print(slack_client.api_call("api.test"))
print(slack_client.api_call("auth.test"))

if slack_client.rtm_connect():

    print(slack_client.api_call("users.list"))

    while True:

        checkEvent = slack_client.rtm_read()

        for event in checkEvent:
            print(event)
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
        ********************************
         (Philip J.) FRY BOT - Futurama
        ********************************

What can the bot do :

"""

"""               ___________
                    METHODS
                  ___________
    bot              : https://api.slack.com/bot-users
    chat.postMessage : https://api.slack.com/methods/chat.postMessage
                       https://api.slack.com/docs/formatting
    rtm.start        : https://api.slack.com/methods/rtm.start
                       https://api.slack.com/rtm

"""