import os
from tkinter import E
import discord
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os 
from discord.ext import tasks
load_dotenv()



client = Bot(command_prefix="p",intents=discord.Intents.all())
token = os.environ['token']



@client.event
async def on_ready():
    print('on ready')
    

@client.command()
async def play(ctx,n:int):
    global voice
    list = ['https://silverstream.radioca.st/;','https://eu8.fastcast4u.com/proxy/clyedupq/?mp=/1','https://node-12.zeno.fm/f4ppurqe3v8uv?rj-ttl=5&rj-tok=AAABfxHdmrcAKB-tQeweQUswGw',
        'https://node-33.zeno.fm/mrkzzr5uyc9uv?rj-ttl=5&rj-tok=AAABfxH07akARF5DKydVCwhuew','https://funasia.streamguys1.com/live4',
        'https://node-22.zeno.fm/rfpf8qec94zuv?rj-ttl=5&rj-tok=AAABfxH3SVAAyTx5-GEYjRSBaw','https://lmil.pc.cdn.bitgravity.com/lmil/live/aajtak_150k/chunklist_ao.m3u8']
    l1 = ["Marathi Mirchi Mumbai","South Asia Mirchi","Patna Mirchi Radio","Radio City hindi","Big FM 106.2","Arjit Singh Song Radio","Aajtak News"]
    if n > len(list) and n<=0:
        await ctx.send("Please enter valid Radio station listed number\nUse `plist` to see available radio stations")
    
    try :
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        print("try_")
        
        #'https://silverstream.radioca.st/;' - marathi
        #'https://eu8.fastcast4u.com/proxy/clyedupq/?mp=/1" - south asia mirchi
        #'https://node-12.zeno.fm/f4ppurqe3v8uv?rj-ttl=5&rj-tok=AAABfxHdmrcAKB-tQeweQUswGw' - patna mirchi radio
        #img-"https://zeno.fm/_next/image/?url=https%3A%2F%2Fimages.zeno.fm%2FI3hxBecKMAIdgPAn41KgC046vj1ymam5PnkecRwzKDI%2Frs%3Afit%3A288%3A288%2Fg%3Ace%3A0%3A0%2FaHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYWd4emZucGxibTh0YzNSaGRITnlNZ3NTQ2tGMWRHaERiR2xsYm5RWWdJQ3c1dk9Cb2dzTUN4SU9VM1JoZEdsdmJsQnliMlpwYkdVWWdJQ3c5cEQ4OFFnTW9nRUVlbVZ1YncvaW1hZ2UvP3Jlc2l6ZT0yODh4Mjg4JnVwZGF0ZWQ9MTY0NTA3OTM5NzAwMA.webp&w=640&q=75"
        #'https://node-33.zeno.fm/mrkzzr5uyc9uv?rj-ttl=5&rj-tok=AAABfxH07akARF5DKydVCwhuew' - radio city hindi
        #img-"https://zeno.fm/_next/image/?url=https%3A%2F%2Fimages.zeno.fm%2F6sN381Cd4Vwi-JB6RBPly_kNT-IoxCVhHTrbgzGNS5U%2Frs%3Afit%3A240%3A240%2Fg%3Ace%3A0%3A0%2FaHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYWd4emZucGxibTh0YzNSaGRITnlNZ3NTQ2tGMWRHaERiR2xsYm5RWWdJQ0F4SkdkdkFzTUN4SU9VM1JoZEdsdmJsQnliMlpwYkdVWWdJRHdpYTJLeWdvTW9nRUVlbVZ1YncvaW1hZ2UvP3Jlc2l6ZT0yNDB4MjQwJnVwZGF0ZWQ9MTY0NDczOTQ0ODAwMA.webp&w=640&q=75"
        #'https://node-22.zeno.fm/rfpf8qec94zuv?rj-ttl=5&rj-tok=AAABfxH3SVAAyTx5-GEYjRSBaw' - arjit singh
        #img - "https://zeno.fm/_next/image/?url=https%3A%2F%2Fimages.zeno.fm%2FNDHR6OWdvxb-YtOE-gEAr9-EXuY5nTtNxKftK25K_8Y%2Frs%3Afit%3A240%3A240%2Fg%3Ace%3A0%3A0%2FaHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYWd4emZucGxibTh0YzNSaGRITnlNZ3NTQ2tGMWRHaERiR2xsYm5RWWdJQ2dzcTdIclFzTUN4SU9VM1JoZEdsdmJsQnliMlpwYkdVWWdJQ1EzWXYybVFvTW9nRUVlbVZ1YncvaW1hZ2UvP3Jlc2l6ZT0yNDB4MjQwJnVwZGF0ZWQ9MTY0NTE0NTg0MDAwMA.webp&w=640&q=75"
        #'https://lmil.pc.cdn.bitgravity.com/lmil/live/aajtak_150k/chunklist_ao.m3u8' - aajtak news
        #img - "https://liveradios.in/wp-content/uploads/aajtak.jpg"
        #'https://funasia.streamguys1.com/live4' - big fm 106.2
        #img - "https://liveradios.in/wp-content/uploads/bignew1-1.jpg"
        async with ctx.typing():
            voice.play(FFmpegPCMAudio(list[n-1]))
        await ctx.send('**Now playing:`{}`**'.format(l1[n-1]))
        
    except Exception as e:
        print(e)
        if str(e) != "Already connected to a voice channel.":
         await ctx.send("The bot is not connected to a voice channel.")
        else:
            voice_client = ctx.message.guild.voice_client
            voice_client.stop()
            async with ctx.typing():
             voice.play(FFmpegPCMAudio(list[n-1]))
            await ctx.send('**Now playing:`{}`**'.format(l1[n-1]))


@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Radio paused")
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@client.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Radio resumed")
    else:
        await ctx.send("The bot was not playing anything before this. Use play command")

@client.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@client.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
       await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@client.command( help='Shows available radio channels')
async def ist(ctx):
    embed = discord.Embed( title="**Available radios**",description="Use pplay {number beside the radio channel} to play the respective channel", color=0xE91E63 )
    embed.add_field( name="**1**", value="Marathi Mirchi Mumbai", inline=False )
    embed.add_field( name="**2** ", value="South Asia Mirchi", inline=False )
    embed.add_field( name="**3**", value="Patna Mirchi Radio", inline=False )
    embed.add_field( name="**4**", value="Radio City hindi", inline=False )
    embed.add_field( name="**5**", value="Big FM 106.2", inline=False )
    embed.add_field( name="**6**", value="Arjit Singh Song Radio", inline=False )
    embed.add_field( name="**7**", value="Aajtak News", inline=False )
    await ctx.send( embed=embed )
   


client.run(token)