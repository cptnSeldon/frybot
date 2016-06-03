"""This is frybot.

A Slack bot that sends Futurama memes and quotes.

Sources:
http://futurama-quotes.tumblr.com/
https://en.wikiquote.org/wiki/Futurama
"""  # Module comment : detailed module explanation.

from time import sleep  # Separate Python stdlib and external imports (PEP8)
import json
from random import randrange

from slackclient import SlackClient
import giphypop


# change this nex time
chan_random = "rand"
chan_general = "gen"
chan_fry = "fry"


class FryBot(object):  # DOCSTRINGS btw triple-double-guote (PEP8) : http://stackoverflow.com/a/9448136/2652657
    """Bot that sends Futurama's Fry memes and quotes."""

    def __init__(self, token):
        self.giphy = giphypop.Giphy()  # Giphy works with public auth, so we use it as is.
        self.sc = SlackClient(token)
        self.channel = chan_fry

    def _fgif(self, event, event_username):  # Private methods/function start wt _(PEP8)
        """Prepare GIF for sending"""
        query = event["text"][5:]
        response = self.giphy.search_list("Futurama", query)
        rand_index = randrange(0, len(response))
        input = response[rand_index]
        return self.sc.api_call("chat.postMessage", as_user="true", channel=self.channel,
                                text="Shut up and take my Gif!",
                                attachments=json.dumps([{"title": "image",
                                                         "image_url": input.media_url}]))

    def _fpict(self, event, event_username):
        """Prepare picture URL for sending"""
        input = "I am a picture " + event["text"][6:]
        return self.sc.api_call("chat.postMessage", as_user="true", channel=self.channel,
                                text="@" + event_username + ": " + input)

    def _fquote(self, event, event_username):
        """Prepare quote for sending"""
        input = "I am a quote " + event["text"][7:]
        return self.sc.api_call("chat.postMessage", as_user="true", channel=self.channel,
                                text="@" + event_username + ": " + input)

    def _parse(self, event):
        """Parse user input"""
        event_username = self.sc.api_call('users.info', user=event["user"])['user']['name']

        if event["text"].startswith("fgif"):
            msg = self._fgif(event, event_username)
        elif event["text"].startswith("fquote"):
            msg = self._fquote(event, event_username)
        elif event["text"].startswith("fpict"):
            msg = self._fpict(event, event_username)
        else:
            return
        print(msg)

    def run(self):
        """Run the bot and treat incoming events"""
        for test in ["api.test", "im.open", "auth.test"]:  # Super pythonic testing stuff
            print(self.sc.api_call(test))

            if self.sc.rtm_connect():	
                print(self.sc.api_call("users.list"))  # to delete
                while True:  # add try
                    for event in self.sc.rtm_read():
                        if "type" in event:
                            if event["type"] == "message" and "text" in event \
                                 and "bot_id" not in event and event["channel"] == self.channel:
                                self._parse(event)
                    sleep(1)
            else:
                raise RuntimeError("Connection failed to Slack platform...")

if __name__ == '__main__':  # behavior "by default" when exec
    fb = FryBot("token")
    try:
        fb.run()
    except KeyboardInterrupt:  # ctrl-c
        print("Bye guyz, I'm out...")