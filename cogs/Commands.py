import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from github import Github
import os


class Commands(commands.Cog):

  def __init__(self, client):
    self.client = client

  serverID = 1011650341982437497

  @commands.command()
  async def hello(self, ctx):
    await ctx.send('shut up!')
    
  @nextcord.slash_command(name="testcommand",description="wabeebabo", guild_ids=[serverID]) 
  async def testcommand(self, interaction: Interaction, message:str, message2:str):
    await interaction.response.send_message(f'Yo mum. Also you typed in "{message}" and "{message2}"')

  @nextcord.slash_command(name="addmailboxmessage",description="Adds a message to the mailbox.", guild_ids=[serverID]) 
  async def addmailboxmessage(self, interaction: Interaction, title:str, message:str):
    await interaction.response.send_message(f'Added "{title}"')
    f = open('SalesData.txt','r')
    ye = f.read()
    f.close()
    my_file = open("SalesData.txt", "w")
    my_file.write(ye + "\n")
    my_file.write(f"{title};{message}")
    my_file = open("SalesData.txt")
    my_file.close()
    
    GotTOKEN = os.environ['GitTOKEN']
    g = Github(GotTOKEN)
    
    repo = g.get_repo("RawZebra/TLL-Aide")
    contents = repo.get_contents("SalesData.txt", ref="test")
    repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="Main")
    


def setup(client):
  client.add_cog(Commands(client))