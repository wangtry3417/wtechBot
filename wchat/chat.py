from cryptography.fernet import Fernet
from random import randint

apiKey = None

def setPrompt(prompt : str):
  return prompt

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
        if prompt == "Hello" or "Hi" or "hi" or "hello":
          fungpt.aigen = "Hello!"
          return fungpt.aigen
        else:
          fungpt.aigen = "Sorry,I don't understand!"
          return fungpt.aigen
      else:
        return "Please input your prompt!"
    else:
      return "You must use the run() first!"
                             
