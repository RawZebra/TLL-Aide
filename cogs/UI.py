import nextcord
from nextcord.ext import commands
from nextcord import Interaction


class Dropdown(nextcord.ui.Select):
  def __init__(self):
    selectoptions = [
      nextcord.SelectOption(label='test', description="it's a test dropdown"),
      nextcord.SelectOption(label='test2', description="it's a test dropdown but the second"),
      nextcord.SelectOption(label='test3', description="it's a test dropdown but the third")
    ]
    super().__init__(placeholder='Select test:', min_values=1, max_values=1, options=selectoptions)
    
    async def callback(interaction: Interaction):
      await interaction.response.edit_message(content='Selected', view=None)
      await interaction.followup.send(f'{interaction.user.mention} selected {self.values[0]}')
      
    self.callback = callback

class DropdownView(nextcord.ui.View):
  def __init__(self):
    super().__init__()
    self.add_item(Dropdown())

class UI(commands.Cog):

  def __init__(self, client):
    self.client = client

  serverID = 1011650341982437497
    
  @nextcord.slash_command(name="dropdown",description="Makes a dropdown", guild_ids=[serverID]) 
  async def dropdown(self, interaction: Interaction):
    view = DropdownView()
    await interaction.response.send_message('Choose one. :>', view=view)
    


def setup(client):
  client.add_cog(UI(client))