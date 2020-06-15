import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'ha bhai ik your name is {message.author.name} and your id is {message.author.id}.')

client.run(TOKEN)

# TODO - recognize gsheet link (public)
# TODO - get cell data using gsheet api
# TODO - use https://pypi.org/project/terminaltables/ and generate table

'''
Table example-
+--------+--------+-----------+
| number | name   | role      |
+--------+--------+-----------+
| 1      | rachit | loser     |
+--------+--------+-----------+
| 2      | mihir  | pro loser |
+--------+--------+-----------+
'''