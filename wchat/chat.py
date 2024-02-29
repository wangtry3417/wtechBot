from cryptography.fernet import Fernet
from random import randint
from nltk.chat.util import Chat, reflections

apiKey = None

def setPrompt(prompt : str):
  return prompt

pairs = [
    [
        r"我需要(.*)",
        ["为什么你觉得你需要%1?", "这对你来说真的很重要吗?", "你可以说说有关%1的更多信息吗?",]
    ],
    [
        r"你不会(.*)吗?",
        ["你为何以为我不会%1？", "试着想象我会%1，然后我们再谈吧。", "你可能会对我是否会%1感到惊讶。",]
    ],
    [
        r"你是(.*)",
        ["为什么你对我是不是%1感兴趣?", "你是否喜欢我是%1?", "你可能只是想知道我是不是%1。", "你为何未明说出我是否%1对你来说意味着什么？"]
    ],
]


class fungpt:
  def __init__(self,intents):
    self.intents = intents
    self.aigen = None
    self.freeime = 3
  @staticmethod
  def run(api_key : str,prompt : str):
    key = "DUBWKuYEugUex8ynVKm-7ctcUmwaV0u0JpzLkoka8_Q="
    fernet = Fernet(key)
    # 解密结果
    data = fernet.decrypt(api_key.encode())
    try:
      if data.decode() == "WTechPass122":
        return fungpt.chat(num=randint(22928,292892),prompt=setPrompt(prompt))
      else:
        return "Your key invaild!"
    except:
      return "Please input your key!"
  @staticmethod
  def chat(num : int,prompt : str):
    if num != None:
      if prompt is not None:
        return "你好，我是FunGPT-turbo!"
        chat = Chat(pairs, reflections)
        return chat.converse(prompt)
      else:
        return "Please input your prompt!"
    else:
      return "You must use the run() first!"
                             
