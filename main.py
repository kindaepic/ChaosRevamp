import colorama
from colorama import Fore, Style, init
import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import requests
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime, sleep
import ctypes
import asyncio
import webbrowser
import subprocess 
#-----------CONFIG-----------#

token = os.getenv("token")
prefix = os.getenv("prefix")
user_id = os.getenv("userid")
streamurl = os.getenv("streamurl")

#----------------------------#
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command(name="help")

print(f"""
{Fore.BLUE}    
 
 ▄████████    ▄█    █▄       ▄████████  ▄██████▄     ▄████████ 
███    ███   ███    ███     ███    ███ ███    ███   ███    ███ 
███    █▀    ███    ███     ███    ███ ███    ███   ███    █▀  
███         ▄███▄▄▄▄███▄▄   ███    ███ ███    ███   ███        
███        ▀▀███▀▀▀▀███▀  ▀███████████ ███    ███ ▀███████████ 
███    █▄    ███    ███     ███    ███ ███    ███          ███ 
███    ███   ███    ███     ███    ███ ███    ███    ▄█    ███ 
████████▀    ███    █▀      ███    █▀   ▀██████▀   ▄████████▀  

                          Version V3 (Revamp)       
                           Made by Axis/Marx
                            {Fore.BLUE}
                            {Fore.RESET}
""")
print(f"""
{Fore.YELLOW}    
Newest Features:
● Better raiding commands
● More customization 
● Fixed bugs/errors
{Fore.RESET}
""")


@bot.event
async def on_connect():
  print(f"""
  {Fore.WHITE}
  {Style.DIM}
  Logged in as: {bot.user.name} #{bot.user.discriminator}
  {Fore.RESET}
  """)
################CHAT COMMANDS################
@bot.command()
async def help(ctx):
  embed=discord.Embed(title="CG Selfbot Commands", description=f"""
**__Chat Commands__**
```
{prefix}help
Shows this message. 
{prefix}serverinfo
Shows the servers stats.
{prefix}pfp <mention>
Gets the profile picture of the mentioned user.
{prefix}clear
Clears all of your message in a chat. Can be used in dms, groupchats and servers.
{prefix}autobump <channelID>
Aliases: a-bump, bump
Automatically sends a bump message to the channel ID.
{prefix}backup
Aliases: friendbackup, friend-backup
Backs up all of your friends.
```
**__Raid Commands__**
```
{prefix}spam <message>
Spams the channel the message was sent in.
{prefix}spamall <message>
Spams all channels in a guild.
{prefix}ghostspam <message>
Aliases: gpsam , gs
Sends and deletes a message repeadetly.
{prefix}channeldelete
Aliases: cdel , chandel , cd
Deletes all channels. 
{prefix}channelcreate <name>
Aliases: ccreate , cc
Creates channels in a guild.
{prefix}rolecreate <name>
Aliases: rcreate , rc
Creates roles in a guild.
{prefix}roledelete
Aliases: rdelete, rd
Deletes all roles in a guild.
{prefix}blankbomb
Aliases: bb
Fills the chat with a blank message.
{prefix}geoip
Aliases: geolocate, iptogeo
Gets info about a certain IP.
{prefix}tokencheck <token>
Checks if a token works.
{prefix}tokeninfo <token>
Gets some info about a Discord token.
```
**__Other Commands__**
```
{prefix}logout
Logs you out of the selfbot.
{prefix}listening <message>
Sets your status to listening. 
{prefix}watching <message>
Sets your status to watching.
{prefix}playing <game>
Sets your status to playing.
{prefix}streaming <message>
Sets your status to streaming.
```
  """, color=0x980E0E)
  embed.set_footer(text="Github: https://github.com/MarxFromCG")
  await ctx.send(embed=embed, delete_after = 20)

@bot.command()
async def serverinfo(ctx):
 await ctx.message.delete() 
 guild = ctx.message.guild
 roles = [role for role in guild.roles]
 channels = [channel for channel in guild.channels]
 categories = [category for category in guild.categories]
 embed = discord.Embed(colour=0Xff0000, timestamp=ctx.message.created_at)
 embed.set_author(name=f"{guild.name}")
 embed.add_field(name=f"**Member Count:**", value=f"{guild.member_count}", inline=False)
 embed.add_field(name=f"**Role Count:**", value=f"{len(roles)}", inline=False)
 embed.add_field(name=f"**Channel Count:**", value=f"{len(channels)}", inline=False)
 embed.add_field(name=f"**Category Count:**", value=f"{len(categories)}", inline=False)
 embed.add_field(name=f"**Guild Region:**", value=f"{guild.region}", inline=False)
 embed.add_field(name=f"**Creation Date:**", value=f"{guild.created_at}", inline=False)
 embed.add_field(name=f"**Owner:**", value=f"{guild.owner}", inline=False)
 embed.set_thumbnail(url=guild.icon_url)
 await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def pfp(ctx, member: discord.Member):
 await ctx.message.delete() 
 member = ctx.author if not member else member
 
 embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
 embed.set_author(name=f"Avatar for {member}")
 embed.set_image(url=member.avatar_url)
 await ctx.send(embed=embed)
@bot.command()
async def clear(ctx):
         channel = ctx.message.channel
         messages = await channel.history(limit=None).flatten()
         for message in messages:
           if message.author == bot.user:
             try:
               await message.delete()
             except:
               pass 
@bot.command(aliases=['bump', 'a-bump'])
async def autobump(ctx, channelid): # 
   await ctx.message.delete()
   count = 0
   while True:
       try:
           count += 1
           channel =  bot.get_channel(int(channelid))
           await channel.send('!d bump')          
           print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
           await asyncio.sleep(7200)
       except Exception as e:
           print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)               
@bot.command(aliases=['friendbackup', 'friend-backup'])
async def backup(ctx): # 
   await ctx.message.delete()
   for friend in bot.user.friends:
      friendlist = (friend.name)+'#'+(friend.discriminator)
      with open('Friends.txt', 'a+') as f:
          f.write(friendlist+"\n" )           
################RAID COMMANDS################
@bot.command()
async def spam(ctx, *, message):
  await ctx.message.delete()
  while True:
    await ctx.send(message)
@bot.command()
async def spamall(ctx, *, message):
 await ctx.message.delete()
 guild = ctx.guild
 while True:
   for channel in guild.text_channels:
     try:
       await channel.send(message)
     except:
       pass
@bot.command(aliases=['cdel', 'chandel', 'cd'])
async def channeldelete(ctx):
 await ctx.message.delete() 
 guild = ctx.guild
 for channel in guild.channels:
   await channel.delete()       
@bot.command(aliases=['gspam', 'gs'])
async def ghostspam(ctx, *, message):
  await ctx.message.delete()
  while True:
    await ctx.send(message, delete_after = 0)
@bot.command(aliases=['cc', 'ccreate'])
async def channelcreate(ctx, *, cname):
 await ctx.message.delete() 
 guild = ctx.guild
 while True:
   await guild.create_text_channel(name=cname)
@bot.command(aliases=['rc', 'rcreate'])
async def rolecreate(ctx, rolename):
  await ctx.message.delete()
  guild = ctx.guild
  while True:
    await guild.create_role(name=rolename, color=discord.Colour(0xB20A0A))
@bot.command(aliases=['bb'])
async def blankbomb(ctx): 
   await ctx.message.delete()
   await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
@bot.command(aliases=['rdelete', 'rd'])
async def roledelete(ctx):
   await ctx.message.delete()
   guild = ctx.guild
   for role in guild.roles:
     try:
       await role.delete()
       print(f"{role.name} was deleted.")
     except:
       print(f"{role.name} was not deleted due to an error or missing permissions.")
@bot.command()
async def tokencheck(ctx, tok):
 await ctx.message.delete()
 headers={
    'Authorization': tok # I'll soon be adding support for bulk checking.
 }
 src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
 try:
    if src.status_code == 200:
        print(f'{Fore.GREEN}Token Works.{Fore.RESET}')
        await ctx.send("""```diff
+ Token Works.```
        """)
    else:
        print(f'{Fore.RED}Invalid Token.{Fore.RESET}')
        await ctx.send("""```diff
- Invalid Token.```
""")
 except Exception:
    print("Unable to connect to discorapp.com")
 
@bot.command(aliases=['tokinfo', 'tdoxx'])
async def tokeninfo(ctx, _token): # 
   await ctx.message.delete()
   headers = {
       'Authorization': _token,
       'Content-Type': 'application/json'
   }     
   try:
       res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
       res = res.json()
       user_id = res['id']
       avatar_id = res['avatar']
       creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
   except:
       print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
   em = discord.Embed(
       description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
   fields = [
       {'name': 'Phone', 'value': res['phone']},
       {'name': 'Flags', 'value': res['flags']},
       {'name': 'MFA?', 'value': res['mfa_enabled']},
       {'name': 'Verified?', 'value': res['verified']},
   ]
   for field in fields:
       if field['value']:
           em.add_field(name=field['name'], value=field['value'], inline=False)
           em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
   return await ctx.send(embed=em)
@bot.command(aliases=['geolocate', 'iptogeo'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # 
   await ctx.message.delete()
   r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
   geo = r.json()
   em = discord.Embed()
   fields = [
       {'name': 'IP', 'value': geo['query']},
       {'name': 'IP Type', 'value': geo['ipType']},
       {'name': 'Country', 'value': geo['country']},
       {'name': 'City', 'value': geo['city']},
       {'name': 'Continent', 'value': geo['continent']},
       {'name': 'IPName', 'value': geo['ipName']},
       {'name': 'ISP', 'value': geo['isp']},
       {'name': 'Latitute', 'value': geo['lat']},
       {'name': 'Longitude', 'value': geo['lon']},
       {'name': 'Region', 'value': geo['region']},
   ]
   for field in fields:
       if field['value']:
           em.add_field(name=field['name'], value=field['value'], inline=True)
   return await ctx.send(embed=em)
################OTHER################
@bot.command()
async def logout(ctx): 
    await ctx.message.delete()
    print(f"{Fore.WHITE} {Style.DIM} Logged out of the selfbot.{Style.RESET_ALL}{Fore.RESET}")
    await bot.logout()
@bot.command()
async def listening(ctx, *, message): 
   await ctx.message.delete()
   await bot.change_presence(
       activity=discord.Activity(
           type=discord.ActivityType.listening,
           name=message,
       ))
   print(f"{Fore.GREEN} Set your listening status to {message}{Fore.RESET}")
 
@bot.command()
async def watching(ctx, *, message): 
   await ctx.message.delete()
   await bot.change_presence(
       activity=discord.Activity(
           type=discord.ActivityType.watching,
           name=message
       ))
   print(f"{Fore.GREEN} Set your watching status to {message}{Fore.RESET}")

@bot.command()
async def streaming(ctx, *, message): 
   await ctx.message.delete()
   stream = discord.Streaming(
       name=message,
       url=streamurl,
   )
   await bot.change_presence(activity=stream)
   print(f"{Fore.GREEN} Set your streaming status to {message} (Redirect: {streamurl}){Fore.RESET}")
 
@bot.command()
async def playing(ctx, *, message): 
   await ctx.message.delete()
   game = discord.Game(
       name=message
   )
   await bot.change_presence(activity=game)
   print(f"{Fore.GREEN} Set your playing status to {message}{Fore.RESET}")

bot.run(token, bot=False)
