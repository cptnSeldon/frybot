from slackclient import SlackClient

"""
http://futurama-quotes.tumblr.com/
"""

# ATTRIBUTES
token = "token"
sc = SlackClient(token)
chan_random = "random"
chan_general = "general"
greetings = "Valentine's day? Crap I forgot to get a girlfriend again!"
zapp = "That Young Man Fills Me With Hope. Plus Some Other Emotions Which Are Weird And Deeply Confusing."
fry1 = "It's Like A Party In My Mouth And Everybody's Throwing Up!"
# PROGRAM
print(sc.api_call("api.test"))
print(sc.api_call("im.open"))
# print(sc.api_call("chat.postMessage", as_user="true:", channel=chan_general, text=greetings))
print(sc.api_call("chat.postMessage", as_user="true:", channel=chan_random, text=fry1))


