from discord import Bot,Embed,Option
import discord
import requests as req
import os

bot = Bot(description="This bot made by WTech.")

@bot.event
async def on_ready():
    print("ok")

@bot.slash_command()
async def about(ctx):
    e = Embed(title="about me",description="""Hello, I am made by wtech inc.
              The link: http://wtechhk.xyz"
              """)
    await ctx.respond(embed=e)

@bot.slash_command(description="To google search",options=[Option(str,description="query",name="query")])
async def ggogle_search(ctx,query):
   res = req.get(url=f"https://google.com/search?q={query}").content
   await ctx.respond(res)

bot.run(os.environ.get("token"))
