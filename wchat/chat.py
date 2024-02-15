from cryptography.fernet import Fernet
from random import randint

apiKey = None
prompt = None

class fungpt:
  def __init__(self,intents):
    self.intents = intents
    self.aigen = None
    self.freeime = 3
  @staticmethod
  def run(self,api_key : str):
    key = "DUBWKuYEugUex8ynVKm-7ctcUmwaV0u0JpzLkoka8_Q="
    fernet = Fernet(key)
    # 解密结果
    data = fernet.decrypt(api_key)
    try:
      if data.decode == "WTechPass122":
        return fungpt.chat(num=randint(22928,292892))
      else:
        return "Your key invaild!"
    except:
      return "Please input your key!"
  @staticmethod
  def chat(self,num : int):
    if num != None:
      if prompt is None:
        if prompt == "Hello" or "Hi" or "hi" or "hello":
          self.aigen = "Hello!"
          return self.aigen
        else:
          self.aigen = "Sorry,I don't understand!"
          return self.aigen
      else:
        return "Please input your prompt!"
    else:
      return "You must use the run() first!"
                             
