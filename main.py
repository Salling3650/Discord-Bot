import discord
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
 
@bot.event
async def on_message(message):
    if(message.channel.id == 924952660862435338):
        await bot.add_reaction(message,
        924955343925149736, 924955456802271252)

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
#TSP_is_a_god command end

#Tank command start
  if message.content.startswith("!tank"):
    Command = "https://tenor.com/view/tank-gif-15070190"
    await message.channel.send(Command)
#Tank command end

#Fuck command start
  if message.content.startswith("!fuck"):
    Fuck = "Fuck, Refuses to elaborate, Refuses to leave"
    await message.channel.send(Fuck)
#Fuck command end

#Potat_is_a_god command start
  if message.content.startswith("Potat is a god"):
    NO = "https://tenor.com/view/religion-bill-wurtz-dont-history-gif-14178134"
    await message.channel.send(NO)
#Potat_is_a_god command end

#The_cake_is_a_lie command start
  if message.content.startswith("The cake is a lie"):
    cake = "https://tenor.com/view/cake-lie-the-cake-is-a-lie-cake-is-a-lie-gif-19992579"
    await message.channel.send(cake)
#The_cake_is_a_lie command end

#Command command start
  if message.content.startswith("!command"):
    Command = "Deez, Ligma, TSP is a god, !tank, !fuck"
    await message.channel.send(Command)
#Command command end

keep_alive()
client.run(os.getenv('TOKEN'))
