import discord
from discord.ext import commands
import json

# Load the token from the config file
with open('config.json') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

class MyCog(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            return
        if message.channel.name == 'chair':
            if message.content != '🪑':
                if not message.author.bot:
                    await message.delete()
                    await message.channel.send('🪑')

async def main():
    async with bot:
        await bot.add_cog(MyCog())
        await bot.start(config['token'])

# Run the bot with the token from the config file
import asyncio
asyncio.run(main())