import discord
import random 
from discord import app_commands
from dotenv import load_dotenv
import os
load_dotenv()  # wczytuje plik .env
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
klient = discord.Client(intents=intents)
tree = app_commands.CommandTree(klient)
def wylosuj_hasla_generator_hasel(dlugosc):
   
    schowek="+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    gotowehala=''
    for i in range(dlugosc):
        gotowehala+=random.choice(schowek)
    return gotowehala
@klient.event
async def on_ready():
    print('nasz bot jest gotowy')
    try:
        await tree.sync()
        print("Komendy slash zsynchronizowane")
    except Exception as e:
        print("Błąd synchronizacji:", e)

@tree.command(name="witaj", description="Przywitaj się z botem")
async def cmd_witaj(interaction: discord.Interaction):
    await interaction.response.send_message("co tam u ciebie słychać")
@tree.command(name="gra", description="Bot opowie, w co grać")
async def cmd_gra(interaction: discord.Interaction):
    await interaction.response.send_message("karty, ponieważ są małe i można w nie wszędzie zagrać i kupić")
@tree.command(name="haslo", description="generuje hasła")
@app_commands.describe(dlugosc='dłógość hasła')
async def cmd_haslo(interaction: discord.Interaction,dlugosc:int): 
    await interaction.response.send_message( wylosuj_hasla_generator_hasel(dlugosc))
   
klient.run(token)
