import nextcord as discord
from nextcord import Interaction, Embed, ButtonStyle
from nextcord.ui import View, Button
import os
from dotenv import load_dotenv
import sys

load_dotenv("run.env")
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

DC_URL = "https://dsc.gg/tejv"
RPC_NAME = "Tejvz ⛦"

def clear_console():
    
    os.system('cls' if os.name == 'nt' else 'clear')

@client.event
async def on_ready():
    clear_console()

    
    diablo_art = r"""
 /$$$$$$$  /$$           /$$       /$$          
| $$__  $$|__/          | $$      | $$          
| $$  \ $$ /$$  /$$$$$$ | $$$$$$$ | $$  /$$$$$$ 
| $$  | $$| $$ |____  $$| $$__  $$| $$ /$$__  $$
| $$  | $$| $$  /$$$$$$$| $$  \ $$| $$| $$  \ $$
| $$  | $$| $$ /$$__  $$| $$  | $$| $$| $$  | $$
| $$$$$$$/| $$|  $$$$$$$| $$$$$$$/| $$|  $$$$$$/
|_______/ |__/ \_______/|_______/ |__/ \______/ 
"""
    PURPLE = "\033[95m"  
    RED = "\033[91m"
    RESET = "\033[0m"

    print(PURPLE + diablo_art + RESET)
    print(RED + "                 dsc.gg/tejvz" + RESET)
    print()
    print(f"          {client.user} Is Online Now.")

    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=RPC_NAME,
        details="on top!!",
        state="dsc.gg/tejv"
    )
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower().startswith("@Diablo#0395"):
        embed = Embed(
            title="Tejv On Top!",
            description="Check out our server once!",
            color=discord.Color.blue()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/916987835230334996/1389191480643424367/standard.gif")
        embed.set_footer(text="Tejv 🪐")

        button = Button(label="Tejv Discord Server", url=DC_URL, style=ButtonStyle.link)
        view = View()
        view.add_item(button)
        await message.channel.send(embed=embed, view=view)

client.run(TOKEN)
