import discord
import requests


with open("keys.txt") as file:
    adatok = file.readlines()
cred = [x.strip() for x in adatok] 

client = discord.Client()
api_key = cred[1]
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith('!weather'):
        varos = msg.split("!weather", 1)[1]
        complete_url = base_url + "appid=" + api_key + "&q=" + varos + "&units=metric"
        x = requests.get(complete_url).json()
        if x["cod"] == "401":
            await message.channel.send("API KULCS hiba")
        if x["cod"] == "404":
            await message.channel.send("Nincs {} nevű város".format(varos))
        if x["cod"] == "429":
            await message.channel.send("Próbálkozz újra 1 perc múlva")
        
        y = x["main"]
        varos = x["name"]
        
        await message.channel.send("{} városban a jelenlegi hőmérséklet: {}°C".format(varos, y["temp"]))
        await message.channel.send("{} városban az érzékelt hőmérséklet: {}°C".format(varos, y["feels_like"]))
        await message.channel.send("{} városban a légnyomás: {}hPa ".format(varos, y["pressure"]))
        await message.channel.send("{} városban a páratartalom: {}%".format(varos, y["humidity"]))
        await message.channel.send("{} városban a láthatóság: {}km".format(varos, x["visibility"]/1000))
        await message.channel.send("{} városban a szél sebbesége: {}m/s".format(varos, x["wind"]["speed"]))
        print(x)
        

client.run(cred[0])