import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

#Deez command start
  if message.content.startswith("Deez"):
    Nuts = "...nuts in your mouth"
    await message.channel.send(Nuts)

  if message.content.startswith("deez"):
    Nuts1 = "...nuts in your mouth"
    await message.channel.send(Nuts1)
#Deez command end

#Ligma command starts
  if message.content.startswith("Ligma"):
    Balls = "...balls"
    await message.channel.send(Balls)

  if message.content.startswith("ligma"):
    Balls1 = "...balls"
    await message.channel.send(Balls1)
#Ligma command ends

#TSP_is_a_god command start
  if message.content.startswith("TSP is a god"):
    Yes = "https://tenor.com/view/breaking-bad-walter-white-youre-goddamn-right-gif-14600753"
    await message.channel.send(Yes)
#Deez command end

#Tank command start
  if message.content.startswith("!tank"):
    Command = "https://tenor.com/view/tank-gif-15070190"
    await message.channel.send(Command)
#Tank command end

#Command command start
  if message.content.startswith("!command"):
    Command = "Deez, Ligma, TSP is a god, !tank"
    await message.channel.send(Command)
#Command command end

keep_alive()
client.run(os.getenv('TOKEN'))
