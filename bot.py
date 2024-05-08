from discord import Bot,Embed,Option
import discord
import requests as req
import os
import nltk
from random import randint,choice
from time import sleep
import asyncio

nltk.download("punkt")
wtechAbout = """
WTech Inc. 是一個科技團隊，主要業務包括泓幣(WCoins)、電腦遊戲販售、wtps://內部協議
泓幣(WCoins)是WTech旗下的貨幣，用於 內部交易
FunGPT 是泓技W Tech Inc. 的首個chatAI 
不過現在因託管問題而停止服務。 \n
泓技服務包括discord-bot服務、網頁服務、軟件服務等。
"""

wtechCS = """
 客服，泓技客戶服務部，customer service, cs，提供泓技服務。
"""

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

@bot.slash_command(name="generate",description="generate some text.")
async def generate_text(ctx):
   statment = randint(0,1)
   displayed_text = ''
   if statment == 1:
       message = await ctx.respond(wtechAbout[0])
       for idx, wa in enumerate(list(wtechAbout)[1:], start=1):
           await asyncio.sleep(1)
           displayed_text += wa
           await message.edit(content=displayed_text)
   else:
       message = await ctx.respond(wtechCS[0])
       for idx, wa in enumerate(list(wtechCS)[1:], start=1):
           await asyncio.sleep(1)
           displayed_text += wa
           await message.edit(content=displayed_text)


bot.run(os.environ.get("token"))
