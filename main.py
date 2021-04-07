import discord
from discord.ext import commands, tasks
import discord.utils
from datetime import datetime
import os
import json
import random
import asyncio
from discord_slash import SlashCommand, SlashContext
client = commands.Bot(command_prefix=',')
client.remove_command('help')
slash = SlashCommand

@client.event
async def on_ready():
    global startdate
    startdate = datetime.now()
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('Type ",help" to get help! e'))
    print('----------------------------\nBot is connected to Discord')


#MODERATION AND LOGS________________________




@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.ban(reason=reason)
    ban = discord.Embed(
        title=f":boom: Banned {user.name}!",
        description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.send(embed=ban)

@client.event
async def on_command_completion(ctx):
    channel = client.get_channel(829067962316750898)
    embed = discord.Embed(colour=discord.Color.green(),
                          title="Command Executed")
    embed.add_field(name="Command:", value=f"`,{ctx.command}`")
    embed.add_field(name="User:", value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name="Channel:",
                    value=f"{ctx.channel} **( <#{ctx.channel.id}> )**")
    await channel.send(embed=embed)


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

@client.event
async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
        deleter = entry.user
    print(f"{deleter.name} deleted message by {message.author.name}")

#FUN COMMANDS _______________________________

@client.command(aliases=['t'])
async def test(ctx):
    await ctx.send('I am alive and working! Type ",h" for help!')


@client.command(aliases=['DM', 'Dm'])
async def dm(ctx, *, args):
    author = ctx.message.author
    await ctx.send(
        "I sent you a DM, if you didn't get anything, maybe turn on DMs :)")
    await author.send(args)


@client.command()
async def say(ctx, *, args, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(args)


@client.command(name='spam',
                help='Spams the input message for x ammount of times')
async def spam(ctx, amount: int, *, message):

    for i in range(amount):
        await ctx.send(message)


@client.command()
async def messagecount(ctx, channel: discord.TextChannel = None):
    await ctx.send(
        '`Beep Boop` I am counting the messages \n**(this may take a while so sit tight while I count**)'
    )

    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("There were **{}** messages in **{}**".format(
        count, channel.mention))


@client.command()
async def randomnumber(ctx, number):
    try:
        arg = random.randint(1, int(number))
    except ValueError:
        await ctx.send("Invalid number")
    else:
        await ctx.send(str(arg))


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
async def servers(ctx):
    await ctx.send(f"I am currently in `{len(client.guilds)}` servers!")

@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])

client.run('ODAzODYyMTc5NTQ2NjYwOTM0.YBD8_g.ZSzwRSnAZQEbZT-0MYULN1vhJmA')
