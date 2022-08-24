import discord
import responses
import os
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import urllib

async def send_message(message, user_message, is_private):
  try:
      response = responses.handle_repsonse(message)
    
      if(response != None):
        await message.author.send(response) if is_private else await message.channel.send(response)
        
  except Exception as e:
    print(e)

def run_discord_bot():
  TOKEN = os.environ['TOKEN']
  client = discord.Client(intents=discord.Intents.all())

  @client.event
  async def on_ready():
    print(f'{client.user} in now running')



  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f"{username}: '{user_message}' ({channel})")

    if user_message.split()[0] == 'GetEntityData':
      #Getting entity data
      target_url = f"https://raw.githubusercontent.com/RawZebra/TheLostLandscapes_data/main/{channel.capitalize()}/EntityData.txt" 
      toReturn = ''
      resource = urllib.request.urlopen(target_url)

      for line in resource:
        print(line)
        if(line.split(b' ')[0] == user_message.split()[1].encode("utf-8")):
          toReturn = line
          print(toReturn)
          break

       #Got entity data
      final = toReturn.decode("utf-8")
      finalS = final.split()
      iconSplit = finalS[7].split(',')[0]
      
      #Getting entity name
      target_url = f"https://raw.githubusercontent.com/RawZebra/TheLostLandscapes_data/main/Lang/en.txt" 
      toReturn = ''
      resource = urllib.request.urlopen(target_url)

      for line in resource:
        print(line)
        if(line.split(b'=')[0] == user_message.split()[1].encode("utf-8")):
          toReturn = line
          break

      #Got entity name
      entityName = toReturn.decode("utf-8").split('=')
      
      print(entityName[1])
      urllib.request.urlretrieve(f'https://github.com/RawZebra/TheLostLandscapes_data/raw/main/Images/{iconSplit}.png',"Images/ico.png")

      font = ImageFont.truetype('Misc/font.ttf', 40)
      bg = Image.open('Images/BG.png')
      ico = Image.open('Images/ico.png')
      ico = ico.resize((113,113))
      bg.paste(ico, (37,27),ico)
      draw = ImageDraw.Draw(bg)
      draw.text((184, 30), entityName[1], (255,255,255), font=font)
      
      bg.save('Images/Final.png')      
      with open('Images/Final.png', 'rb') as f:
        picture = discord.File(f)
      
      await message.channel.send(final,file=picture)

    if user_message.split()[0] == 'addText':
      f = open('SalesData.txt','r')
      ye = f.read()
      f.close()
      my_file = open("SalesData.txt", "w")
      my_file.write(ye + "\n")
      my_file.write("Second Line")
      my_file = open("SalesData.txt")

      content = my_file.read()

      my_file.close()

      print(content)
      
    await send_message(message, user_message, is_private=False)
    
  client.run(TOKEN)
