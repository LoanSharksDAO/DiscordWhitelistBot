from discord.ext import commands

bot = commands.Bot(command_prefix=['f.','F.'], help_command=None)

#Stat Commands
@bot.command()
async def rarity(ctx):
    await fives_obj.fives_rarity(ctx)

@bot.command()
async def help(ctx):
    await fives_obj.fives_info(ctx)

bot.run("ODg2ODcxNzIzMzk0MzYzNDAz.YT75qA.JFPRrW1Cgxj52A2MXbxZ2DspmYg")