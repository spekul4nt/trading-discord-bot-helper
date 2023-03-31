import discord
from discord.ext import commands


intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

user_channels = {}
guild_id = 923681805624815729  # замените на ID вашего сервера
category_name = 'Wasze dzienniki'

@bot.command(name='dziennik')
async def dziennik(ctx):
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        ctx.author: discord.PermissionOverwrite(read_messages=True)
    }
    category = discord.utils.get(ctx.guild.categories, name='Wasze dzienniki')
    channel = await ctx.guild.create_text_channel(name=f'dziennik-{ctx.author.name}', category=category, overwrites=overwrites, reason='Stworzono prywatny dziennik')
    await ctx.send(f'Twoj prywatny dziennik zostal stworzony na kanale {channel.mention}!')

    # Увеличиваем счетчик каналов пользователя
    if ctx.author.id not in user_channels:
        user_channels[ctx.author.id] = 1
    else:
        user_channels[ctx.author.id] += 1

bot.run('BOT_TOKEN')
