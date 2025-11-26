import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random
import asyncio
# ENV
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = os.getenv("DISCORD_SERVER_ID")


# COGS
# from cogs.test_cog import information



bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"Bot logged as {bot.user}")

@bot.slash_command(description="Get your random number")
async def random_number(interaction: nextcord.Interaction):
    n = 100
    ran_num = random.randint(1,n)
    if ran_num % 10 == 0: # every number that is devided by 10 -> 10,20,30,40, etc.
        await interaction.send(f"{interaction.user.mention} WON A LOTTERY WITH {ran_num}!")
    else:
        await interaction.send(f"{interaction.user.mention} lucky number is {ran_num}!")

async def main():
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run((main()))