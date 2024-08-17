import requests
from twitchio.ext import commands

# Twitch bot configuration
bot_token = 'YOUR_TWITCH_BOT_TOKEN'
bot_prefix = '!'
channel_name = 'ProgrammerSockz'

# Server API endpoint
api_endpoint = 'YOUR_API_ENDPOINT'

# Twitch bot event handlers
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=bot_token, prefix=bot_prefix, initial_channels=[channel_name])

    async def event_ready(self):
        print(f'Bot connected to Twitch channel: {channel_name}')

    async def event_bits(self, channel, user, bits):
        # Send API call to the server
        payload = {'user': user.name, 'bits': bits}
        response = requests.post(api_endpoint, json=payload)
        if response.status_code == 200:
            print(f'Successfully sent API call for {bits} bits from {user.name}')
        else:
            print(f'Failed to send API call for {bits} bits from {user.name}')

# Create and run the Twitch bot
bot = Bot()
bot.run()