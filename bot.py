from discord import Bot,Embed,Option
import discord
import requests as req
import os
import nltk
from random import randint,choice
from time import sleep
import asyncio

import fastapi_poe as fp

import threading

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

class EchoBot(fp.PoeBot):
    async def get_response(self, request: fp.QueryRequest):
        last_message = request.query[-1].content
        tokens = nltk.word_tokenize(last_message)
        if any(token in wtechAbout for token in tokens):
            for wa in list(wtechAbout):
                yield fp.PartialResponse(text=wa)
                sleep(0.1)
        elif any(token in wtechCS for token in tokens):
          for wa in list(wtechCS):
            yield fp.PartialResponse(text=wa)
            sleep(0.1)
        else:
            yield fp.PartialResponse(text="No sir!.")
            sleep(0.1)

@bot.slash_command()
async def about(ctx):
    e = Embed(title="about me",description="""Hello, I am made by wtech inc.
              The link: http://wtechhk.xyz"
              """)
    await ctx.respond(embed=e)

def run_poe():
   fp.run(EchoBot(),access_key="PSwr0cAY2heLRrHjikTwEpf8BDrygS49")


thread1 = threading.Thread(target=run_poe)

thread1.start()
