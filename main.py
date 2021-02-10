import discord
from discord.ext import commands
from utils import *
from func import *

intents = discord.Intents(messages=True,
                          guilds=True,
                          reactions=True,
                          members=True,
                          presences=True)

TOKEN= open("token.txt","r").read()
Bot = commands.Bot(command_prefix='xx ')
game= Game()


@Bot.event
async def on_ready():
    print("I'm ready :)")


async def on_member_join(member):
    channel=discord.utils.get(member.guild.text_channels,name="yeni_katilim")
    await  channel.send(f"{member}  katıldı. Hos Geldin! :)")
   # print(f"{member} aramıza katıldı. Hos Geldin! :)")


async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="ayrilanlar")
    await  channel.send(f"{member} aramızdan ayrıldı :(")
    #print(f"{member} aramızdan ayrıldı :(")


@Bot.command(aliases=["game","oyun"])
async def test(ctx,*args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('Basarili')


Bot.run(TOKEN)
