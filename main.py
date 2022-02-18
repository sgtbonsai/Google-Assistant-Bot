import discord
from discord.ext import commands
import discord.utils
from datetime import datetime
import os
import json
import random
import asyncio
import logging
import uuid
import logging
client = commands.Bot(command_prefix='e!')
client.remove_command('help')
@client.event
async def on_ready():
    global startdate
    startdate = datetime.now()
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{servers} servers and {members} members'
    ))
    print('Bot is connected to Discord')

#SLASH COMMANDS _________

  

#FUN COMMANDS _______________________________

@client.command()
async def invite(ctx):
 embed=discord.Embed(title="Invite Me!", description="Thank you for considering me for a new server!", color=discord.Color.orange(), icon_url="https://cdn.discordapp.com/avatars/803862179546660934/bd4c3105280b890b53b38f6812ab45b0.png?size=1024")
 embed.add_field(name="Thank You for supporting me!", value='[Invte Eclipse Today!](https://discord.com/api/oauth2/authorize?client_id=803862179546660934&permissions=8&scope=bot)', inline=True)
 await ctx.send(embed=embed)

@client.command(aliases=["t", "Test", "T", "areyouworkingyouidiot?"])
async def test(ctx):
    embed=discord.Embed(title="The test is successful!", description='For help, please do "e!help"', color=discord.Color.orange())
    await ctx.send(embed=embed)

@client.command(aliases=['DM', 'Dm'])
async def dm(ctx, *, args):
    author = ctx.message.author
    await ctx.send(
        "I sent you a DM, if you didn't get anything, maybe turn on DMs :)")
    await author.send(args)

@client.command()
async def say(ctx, *, args, amount=1):
    await ctx.channel.purge(limit=amount)
    embed=discord.Embed(title=f"{ctx.author.mention} made me say something!", description=" ", color=discord.Color.orange())
    embed.add_field(name=f'"{args}"', value="Look, they said it, not me.", inline=True)
    await ctx.send(embed=embed)
    
@client.command()
async def purge(self, ctx, amount=int):
    await ctx.channel.purge(amount=amount+1)

@client.command()
async def messagecount(ctx, channel: discord.TextChannel = None):
    await ctx.send(
        '`Beep Boop` I am counting the messages \n**(this may take a while so sit tight while I count**)'
    )

    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("There were **{}** messages in **{}**".format(count, channel.mention))

@client.command()
async def AmongUs(ctx):
  await ctx.send('<@701215176921448508> sus')

@client.command()
async def RedCup(ctx):
  await ctx.send("this is a red cup lmao i'm tired and the voices are getting closer and closer every day please help I can't take it anymore pleas HELP!!!!")

@client.command()
async def AppleCloth(ctx):
  AppleCloth=discord.Embed(title="Apple Cloth", description="Made with soft, nonabrasive material, the Polishing Cloth cleans any Apple display, including nano-texture glass, safely and effectively.", color=discord.Color.orange())
  AppleCloth.set_thumbnail(url="https://cdn.discordapp.com/attachments/805878097756684288/902322733097058344/F16E07ED-7249-4FE7-AE3D-B4F5B47D0CA7.png")
  AppleCloth.add_field(name="Get your Apple Cloth for only $20", value='[Get your Apple Cloth here!!](https://www.apple.com/shop/product/MM6F3AM/A/polishing-cloth)', inline=True)
  await ctx.send(embed=AppleCloth)

@client.command(aliases = ["birthday"])
async def Birthday(ctx):
  await ctx.send('My birthday is `January 27th, 2021 at 12:08PM CST`')

@client.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content
    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

@client.command()
async def mock(ctx, *, message):
    out = ''.join(random.choice((str.upper, str.lower))(c) for c in message)
    await ctx.send(out)

@client.command()
async def ping(ctx):
  embed=discord.Embed(colour=discord.Color.green(), title="I shall now reveal my ping 😳", description=" ")
  embed.add_field(name=f"My ping is {round(client.latency * 1000)}ms", value="There, I revealed my ping, now what else do you want me to do?", inline=False)
  await ctx.send(embed=embed)
  
#MODERATION AND LOGS________________________

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.ban(reason=reason)
    ban = discord.Embed(
        colour=discord.Color.orange(),
        title=f":boom: Banned {user.name}!",
        description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.send(embed=ban)

@client.event
async def on_command_completion(ctx):
  channel=discord.utils.get(ctx.guild.text_channels, name="logs")
  log=discord.Embed(colour=discord.Colour.green(), title="Command Executed!")
  log.add_field(name="Command", value=f"`e!{ctx.command}`", inline=False)
  log.add_field(name="User:", value=f"{ctx.author.mention}", inline=False)
  log.add_field(name="Channel:", value=f"{ctx.channel} **( <#{ctx.channel.id}> )**")
  await channel.send(embed=log)
    
@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.green(),
                          timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(
        name="Created Account On:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Joined Server On:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:",
                    value="".join([role.mention for role in roles]),
                    inline=True)
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)
   
@client.command()
async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
    roleobject = discord.utils.get(ctx.message.guild.roles, id=847573758695833671)
    await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
    await user.add_roles(roleobject)
    if unit == "s":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m":
        wait = 60 * duration
        await asyncio.sleep(wait)
    await user.remove_roles(roleobject)
    await ctx.send(f":white_check_mark: {user} was unmuted")  
    
#MATH____________________________

@client.command()
async def add(ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = `{eval(operation)}`')


@client.command()
async def sub(ctx, *nums):
    operation = " - ".join(nums)
    await ctx.send(f'{operation} = `{eval(operation)}`')


@client.command()
async def multiply(ctx, *nums):
    operation = " * ".join(nums)
    await ctx.send(f'{operation} = `{eval(operation)}`')


@client.command()
async def divide(ctx, *nums):
    operation = " / ".join(nums)
    await ctx.send(f'{operation} = `{eval(operation)}`')

@client.command()
async def count(ctx):
  await ctx.send('1')

#HELP-------------------------------------

@client.command(aliases=['h', 'commands'])
async def help(ctx):
  author = ctx.message.author
  embed = discord.Embed(colour=discord.Colour.orange(),
                        title="List Of Commands",
                        description="")
  embed.set_author(name="Remember, my prefix is 'b!'", icon_url="")
  embed.set_image(url="")
  embed.set_thumbnail(url="")
  embed.add_field(name="Help",
                  value="DMs you with this embed\n Usage: \n`b!dm <message here>`",
                  inline=True)
  embed.add_field(name="Servers",
                  value="Tells you how many servers i'm in\n Usage: \n`b!servers`",
                  inline=True)
  embed.add_field(name="Say",
                  value="Says the thing you want me to say\n Usage: \n`b!say <message here>`",
                  inline=True)
  embed.add_field(name="Userinfo",
                  value="Responds with the info of the stated user\n Usage: \n`b!userinfo <id>`",
                  inline=True)
  embed.add_field(name="Add",
                  value="Adds the stated numbers\n Usage: \n`b!add <number number>`",
                  inline=True) 
  embed.add_field(name="Subtract",
                  value="Subtracts the stated numbers\n Usage: \n`b!subtract <number number>`",
                  inline=True)
  embed.add_field(name="Multiply",
                  value="Multiplies the stated numbers\n Usage: \n`b!multiply <number number>`",
                  inline=True)
  embed.add_field(name="Divide",
                  value="Divides the stated numbers\n Usage: \n`b!divide <number number>`",
                  inline=True)
  embed.add_field(name="Ban",
                  value="Bans the stated user\n Usage: \n`b!ban <user> <reason>`",
                  inline=True)
  embed.add_field(name="Messagecount",
                  value="Counts the messages in the stated channel\n Usage: \n`b!messagecount <channel>`",
                  inline=True)
  embed.add_field(name="Invite",
                  value="Shows the invite link for Eclipse\n Usage: \n`b!invite`",
                  inline=True)
  embed.add_field(name="RPS",
                  value="Play 'rock paper scissors' with Eclipse!/n Usage: /n`b!rps <rock, paper, or scissors>`",
                  inline=True)
  embed.add_field(name="Mock",
                  value="mAkE eCliPse mOck A qUoTe/n Usage: /n `b!mock <message/quote here>`",
                  inline=True)
  embed.add_field(name="Hidden Commands",
                  value="There are some hidden commands\n Usage: \n`b!<hidden command> good luck :)`",
                  inline=True)
  embed.set_footer(text="Coded by sgtbonsai in collaboration with Daniel Kravec")
  await ctx.send(embed=embed)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



my_secret = os.environ['token']
client.run(my_secret)