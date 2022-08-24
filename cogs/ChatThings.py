import nextcord
from nextcord.ui import Button, View
from nextcord.ext import commands
from nextcord import Interaction
import responses
import bot
import os
from PIL import Image, ImageDraw, ImageFont
import urllib

class ChatThings(commands.Cog):

  def __init__(self,client):
    self.client = client

    
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.client.user:
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
          if(line.split(b' ')[0] == user_message.split()[1].encode("utf-8")):
            toReturn = line
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
          picture = nextcord.File(f)
      
        await message.channel.send(final,file=picture)

    if user_message.split()[0] == 'addText':
        f = open('SalesData.txt','r')
        ye = f.read()
        f.close()
        my_file = open("SalesData.txt", "w")
        my_file.write(ye + "\n")
        my_file.write("tesing")
        my_file = open("SalesData.txt")
  
        content = my_file.read()

        my_file.close()

      
        await message.channel.send('Added "testing" to SalesData.txt')

    if user_message == 'Add discount':
        #ButtonFunctions
        async def btn_callback(interaction):
          full_username = f'{interaction.user.name}#{interaction.user.discriminator}'
          if(full_username == username):
            await interaction.response.edit_message(content='Button was pressed', view=None)
            await interaction.followup.send(f'{interaction.user.mention} Set to set')
          else:
            await interaction.response.send_message(f'{interaction.user.mention}, this is not your command.\nBuzz off!')
          
        async def btn_callback2(interaction):
          full_username = f'{interaction.user.name}#{interaction.user.discriminator}'
          if(full_username == username):
            await interaction.response.edit_message(content='Button was pressed', view=None)
            await interaction.followup.send(f'{interaction.user.mention} Set to persent')
          else:
            await interaction.response.send_message(f'{interaction.user.mention}, this is not your command.\nBuzz off!')
        #myEmoji = '<:Baby_Thumpies_Concept:1011916486836760626>'
        #myEmojiBass = '<:bass:1011916577500823602>'
        button1 = Button(label="Set", style=nextcord.ButtonStyle.green)
        button2 = Button(label="Persent", style=nextcord.ButtonStyle.green)

        button1.callback = btn_callback
        button2.callback = btn_callback2
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        await message.channel.send('Choose discount type', view=view)
        #await message.delete()
      
    await bot.send_message(message, user_message, is_private=False)


def setup(client):
  client.add_cog(ChatThings(client))