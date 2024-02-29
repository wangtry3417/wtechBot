from cryptography.fernet import Fernet
from random import randint
from nltk.chat.util import Chat, reflections

apiKey = None

def setPrompt(prompt : str):
  return prompt

pairs = (
    (
        r"We (.*)",
        (
            "What do you mean, 'we'?",
            "Don't include me in that!",
            "I wouldn't be so sure about that.",
        ),
    ),
    (
        r"You should (.*)",
        ("Don't tell me what to do, buddy.", "Really? I should, should I?"),
    ),
    (
        r"You\'re(.*)",
        (
            "More like YOU'RE %1!",
            "Hah! Look who's talking.",
            "Come over here and tell me I'm %1.",
        ),
    ),
    (
        r"You are(.*)",
        (
            "More like YOU'RE %1!",
            "Hah! Look who's talking.",
            "Come over here and tell me I'm %1.",
        ),
    ),
    (
        r"I can\'t(.*)",
        (
            "You do sound like the type who can't %1.",
            "Hear that splashing sound? That's my heart bleeding for you.",
            "Tell somebody who might actually care.",
        ),
    ),
    (
        r"I think (.*)",
        (
            "I wouldn't think too hard if I were you.",
            "You actually think? I'd never have guessed...",
        ),
    ),
    (
        r"I (.*)",
        (
            "I'm getting a bit tired of hearing about you.",
            "How about we talk about me instead?",
            "Me, me, me... Frankly, I don't care.",
        ),
    ),
    (
        r"How (.*)",
        (
            "How do you think?",
            "Take a wild guess.",
            "I'm not even going to dignify that with an answer.",
        ),
    ),
    (r"What (.*)", ("Do I look like an encyclopedia?", "Figure it out yourself.")),
    (
        r"Why (.*)",
        (
            "Why not?",
            "That's so obvious I thought even you'd have already figured it out.",
        ),
    ),
    (
        r"(.*)shut up(.*)",
        (
            "Make me.",
            "Getting angry at a feeble NLP assignment? Somebody's losing it.",
            "Say that again, I dare you.",
        ),
    ),
    (
        r"Shut up(.*)",
        (
            "Make me.",
            "Getting angry at a feeble NLP assignment? Somebody's losing it.",
            "Say that again, I dare you.",
        ),
    ),
    (
        r"Hello(.*)",
        ("Oh good, somebody else to talk to. Joy.", "'Hello'? How original..."),
    ),
    (
        r"(.*)",
        (
            "I'm getting bored here. Become more interesting.",
            "Either become more thrilling or get lost, buddy.",
            "Change the subject before I die of fatal boredom.",
        ),
    ),
)

rude_chatbot = Chat(pairs, reflections)

class fungpt:
  def __init__(self,intents):
    self.intents = intents
    self.aigen = None
    self.freeime = 3
  @staticmethod
  def run(api_key : str):
    key = "DUBWKuYEugUex8ynVKm-7ctcUmwaV0u0JpzLkoka8_Q="
    fernet = Fernet(key)
    # 解密结果
    data = fernet.decrypt(api_key.encode())
    try:
      if data.decode() == "WTechPass122":
        return fungpt.chat(num=randint(22928,292892))
      else:
        return "Your key invaild!"
    except:
      return "Please input your key!"
  @staticmethod
  def chat(num : int):
    if num != None:
      print("Hello, I am funGPT-turbo")
      print("Talk to the program by typing in plain English, using normal upper-")
      print('and lower-case letters and punctuation.  Enter "quit" when done.')
      print("=" * 72)
    else:
      return "You must use the run() first!"
                             
