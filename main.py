import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='sala', help='Cria um canal de voz para nova sala de estudos')
async def nova_sala(context, channel_name=None):
    if channel_name is None:
        await context.send('Ops, faltou o nome da sala! Utilize o comando `!sala <nome_da_sala>`')
    else:
        guild = context.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            category = [category for category in guild.categories if category.name.lower() == 'estudos'][0]
            await guild.create_voice_channel(channel_name, category=category)
            await context.send(f'Sala de estudos {channel_name} criada!')


bot.run(TOKEN)
