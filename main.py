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

#Bushpotato command starts
  if message.content.startswith("Bushpotato is a mod"):
    Mod = "https://tenor.com/view/thats-right-baby-gru-steve-carell-despicable-me2-thats-correct-gif-16561725"
    await message.channel.send(Mod)

  if message.content.startswith("bushpotato is a mod"):
    mod = "https://tenor.com/view/thats-right-baby-gru-steve-carell-despicable-me2-thats-correct-gif-16561725"
    await message.channel.send(mod)
#Bushpotato command ends

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

#Deez command start
  if message.content.startswith("Wilma"):
    Cock = "...cock fit in your mouth"
    await message.channel.send(Cock)

  if message.content.startswith("wilma"):
    Cock1 = "...cock fit in your mouth"
    await message.channel.send(Cock1)
#Deez command end

#Tax evasion command start
  if message.content.startswith("pls tax evasion"):
    Tax = "https://store.steampowered.com/app/1205450/Turnip_Boy_Commits_Tax_Evasion/"
    await message.channel.send(Tax)

  if message.content.startswith("Pls tax evasion"):
    Tax1 = "https://store.steampowered.com/app/1205450/Turnip_Boy_Commits_Tax_Evasion/"
    await message.channel.send(Tax1)
#Tax evasion command end

#Offended command starts
  if message.content.startswith("I’m offended"):
    Offended = "https://tenor.com/view/disney-penis-go-fuck-yourself-dick-gif-15801892"
    await message.channel.send(Offended)

  if message.content.startswith("I'm offended"):
    Offended1 = "https://tenor.com/view/disney-penis-go-fuck-yourself-dick-gif-15801892"
    await message.channel.send(Offended1)
#Offended command ends

#Simp command start
  if message.content.startswith("!simp"):
    Simp = "https://tenor.com/view/simp-pewdiepie-pewdipie-simp-meme-funny-gif-19594363"
    await message.channel.send(Simp)
#Simp command end

#8chan command starts
  if message.content.startswith("Pls 8chan"):
    help = "https://tenor.com/view/stop-it-get-some-help-gif-15058124"
    await message.channel.send(help)

  if message.content.startswith("pls 8chan"):
    help1 = "https://tenor.com/view/stop-it-get-some-help-gif-15058124"
    await message.channel.send(help1)
#8chan command ends

#Depressed command start
  if message.content.startswith("!depressed"):
    goodbye = "https://tenor.com/view/pepe-dead-death-boom-4chan-gif-20425333"
    await message.channel.send(goodbye)
#Depressed command end

#Your mom command start
  if message.content.startswith("I fucked"):
    mom = "https://tenor.com/view/your-mom-mother-mom-50cent-50central-gif-10547237"
    await message.channel.send(mom)

  if message.content.startswith("!yourmom"):
    mom1 = "https://tenor.com/view/your-mother-great-argument-however-megamind-your-mom-yo-mama-gif-22994712"
    await message.channel.send(mom1)
#Your mom command end

#Goodbye command start
  if message.content.startswith("!goodbye"):
    goodbye = "https://tenor.com/view/no-country-for-old-men-shower-curtain-gif-22181443"
    await message.channel.send(goodbye)
#Goodbye command end

#Command command start
  if message.content.startswith("!command"):
    Command = "Deez, Ligma, Wilma, TSP is a god, !tank, !fuck, !simp, !goodbye, !depressed, I'm offended"
    await message.channel.send(Command)
#Command command end

keep_alive()
client.run(os.getenv('TOKEN'))
