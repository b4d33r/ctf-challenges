import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def start(ctx):
    await ctx.send("Ajeya weld fin nta?")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check, timeout=30)

        if message.content.lower() == "manik":
            await ctx.send(
                "Explore b4d33r’s connections in the CTF server. You may uncover a hidden detail."
            )
        else:
            await ctx.send("Sir f7alk!")
    except asyncio.TimeoutError:
        await ctx.send("You took too long to reply.")


bot.run('MTM3MDIwNTk1NTM2MjY1MjMwMg.GPbprw.3P366Au1jpkdfsAr4jpxs1u-ouhFOPvSioIfyE')
