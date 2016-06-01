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
giphy_public_key = "dc6zaTOxFJmzC"
# PROGRAM
# print(sc.api_call("api.test"))
# print(sc.api_call("im.open"))
# print(sc.api_call("chat.postMessage", as_user="true:", channel=chan_general, text=greetings))
# print(sc.api_call("chat.postMessage", as_user="true:", channel=chan_random, text=fry1))

""" METHODS """
# DETECT KEYWORD


def detect_keyword(event):
    # retrieve user info
    user_info = slack_client.api_call('users.info', user=event["user"])
    user_name = user_info['user']['name']
    print(user_name)
    # actual test
    if event["text"].startswith("fgif"):
        print(slack_client.api_call("chat.postMessage", as_user="true", channel=chan_fry,
                                    text="Shut up and take my Gif!\nhttp://i.giphy.com/rZ0JTegzdn5pC.gif"))

    elif event["text"].startswith("fquote"):
        print(slack_client.api_call("chat.postMessage", as_user="true", channel=chan_fry,
                                    text="@"+user_name+": "+fquote(event)))

    elif event["text"].startswith("fpict"):
        print(slack_client.api_call("chat.postMessage", as_user="true", channel=chan_fry,
                                    text="@"+user_name+": "+fpict(event)))


# SEND GIF
def fgif(parameter):
    query = parameter["text"][5:]
    query_ = query.replace(" ", "+")
    response = requests.get("http://api.giphy.com/v1/gifs/search?q=futurama"+query+"&api_key="+giphy_public_key)
    #return "I am a gif of " + query
    return response

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
