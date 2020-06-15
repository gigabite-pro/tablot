import discord
import os
from dotenv import load_dotenv
from terminaltables import AsciiTable

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# table data
tableData = [
    ['number', 'name', 'role'],
    ['1', 'rachit gupta', 'loser'],
    ['2', 'mihir aggarwal', 'pro loser']
]

table = AsciiTable(tableData)

@client.event
async def on_ready():
    print('i\'m ready to get back to work')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'```{table.table}```')

client.run(TOKEN)

# TODO - recognize gsheet link (public)
# TODO - get cell data using gsheet api
# TODO - use https://pypi.org/project/terminaltables/ and generate table
