import discord
from discord.ext import tasks, commands
import random

################################ load env

debugging = 1
if debugging == 0:
    envLocation = input('Enter name of env file. Press enter if "data.env"')
else:
    envLocation = ''

if envLocation == '': envLocation = 'data.env'
with open(envLocation) as dotenv:
    tokens = dotenv.readlines()
discordToken = tokens[0]

################################ discord setup

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$',intents=intents)

################################ ready message

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

################################ place to set loops to run

class MyCog(commands.Cog):
    def __init__(self):
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1

################################ message

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$discovendor'):
        await message.channel.send('Hello! I am still running. Thanks for checking in on me.')

################################ command declarations



################################ do not alter below this line

client.run(discordToken)
