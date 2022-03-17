from twitchio.ext import commands
import os

class Bot(commands.Bot):

    # Initialising bot
    def __init__(self):
        super().__init__(token = os.environ.get("OAUTH_TOKEN"), prefix = os.environ.get("BOT_PREFIX"), initial_channels = [os.environ.get("CHANNEL_NAME")], 
            client_id = os.environ.get("CLIENT_ID"), nick = os.environ.get("BOT_USERNAME"))

    # Function for bot to let us know it's ready setting up
    async def event_ready(self):
        print("Bot is ready, logged in as: ", os.environ.get("BOT_USERNAME"))

    # Sends a message into the chat
    async def event_message(self, message):
        print("Sending message: \n", message)
        await self.handle_commands(message)