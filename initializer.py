import os

class Config:

    def __init__(self):
        self.bot_nick = os.environ['TWITCH_BOT_NICK']
        self.token = os.environ['TWITCH_TOKEN']
        self.client_id = os.environ['TWITCH_CLIENT_ID']
        self.prefix = os.environ['TWITCH_PREFIX']
        self.channel = os.environ['TWITCH_CHANNEL']

        
class Initializer:
    def __init__(self):
        self.cfg = Config()