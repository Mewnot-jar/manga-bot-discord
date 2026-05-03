import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f"Conectado exitosamente como {bot.user.name}")

async def main():
    async with bot:
        await bot.load_extension('cogs.manga_cog')
        await bot.load_extension('cogs.favoritos_cog')
        
        await bot.start(TOKEN)

@bot.command()
async def ping(ctx):
    await ctx.send("¡Pong! Sí te estoy leyendo.")

if __name__ == '__main__':
    asyncio.run(main())