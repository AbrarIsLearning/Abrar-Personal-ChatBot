import discord
from discord.ext import commands
import random

#Set the Bot Token here
botToken = "CHANGE ME"

#Client is the variable and sets the prefix for the bot, im not too sure what the intents part do
client = commands.Bot(command_prefix = "r!", intents=discord.Intents.all())

#This will just tell me in the console if the bot is online and working
@client.command
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('a video game'))
    print("Peekaboo!")

#Tells me the connection of the bot using f-strings
@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

#Basic Message. User: r!hello, Bot: hey
@client.command()
async def hello(ctx):
    await ctx.send("hey")

#Learning how to use DICTIONARIES
#Alias is like adding a second name or
#calling it by a diff name. A nickname/alternate command of sort. 
#NOTE: Add all the Combos from the F-Ryougi page on Mizummi
@client.command(aliases=["FrogCombo"])
async def FrogCombos(ctx, combo:str = None):
    comboDict = {
        "1": "(2A) > 5B > 2B > 3C > 236A~236[A]~236A (Outside of the corner input the last 236A as 214A)",
        "2": "(2A) > 5B > 2B > 3C > 236A~236[A]~236A > 236C > jBC > jBC > AT/j.236B",
        "3": "(2A) > 5B > 2B > 5C > 236B~236B~236B, 2A/2B > 5C > j.BC > j.BC > AT/j.236B [This is your BnB]",
        "4": "4C > 22A, 2B > 5C > j.BC > j.BC > j.236B",
        "5": "(2A) > 5B > 2B > 5C > 236B~236B~236C > IH > j.BC > j.BC > j.236C",
        "6":"5B (AA) > 214C > 2A > 5B > j.BC > dj.BC > j.236B"
    }
    #Two guards are setup. One for no input and one for placing a value bigger or smaller then the the dictionary
    if combo is None:
        return await ctx.send("Try the command again but place a number between 1-6. Each number is a combo going from easiest to hardest")
    if combo == "0" or combo > "6":
        return await ctx.send("You inputted a value that is lower or higher then the combo challenges stored. There is only Combo Challenges 1-6 stored at this moment")

    await ctx.send("Don't forget to do it on P2 side as well: " + comboDict[combo])


#Custom help command with r!commandList. A pun/play on words of a Command List found in various 2D Fighting Games
#The Command List in those games would tell you what moves and attacks your character had access to. Same premise here
#but instead of attacks it's just a list of inputs the bot will take
@client.command(aliases=["commandlist"])
async def commandList(ctx):
    await ctx.send("""```Here are the commands for the bot
r!hello: Ryougi say Hello
r!FrogCombos/FrogCombo: Full Moon Ryougi Combo Trials 1-6. (Ex. r!FrogCombos 1)
r!ping: Get the latency of the bot
```""")

client.run(botToken)