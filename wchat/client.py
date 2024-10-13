import socketio,asyncio,time
from colorama import init,Fore

init(autoreset=True)

class Client:
  def __init__(self,client_name):
    self.server_url = "https://sites.wtechhk.xyz"
    self.sio = socketio.AsyncClient()
    self.client_name = client_name

    #設置消息控制和時間
    self.last_message_time = 0
    self.message_cooldown = 1.0 #設置消息冷卻時間為1秒
    self.last_sent_message = None
    
    #事件處理器（字典）
    self.event_handlers = {}

    self.sio.on("connect",self._on_connect)
    self.sio.on("disconnect",self._on_disconnect)
    self.sio.on("chatMessage",self._on_chat_message)

  #事件裝飾器設置
  def on(self,event):
      def wrapper(func):
        self.event_handlers[event] = func
        return func
      return wrapper
    #Connect to socketIO server
    async def connect(self):
      await self.sio.connect(self.server_url)
    #Disconnect to socketIO server
    async def disconnect(self):
      await self.sio.disconnect()

    #Send msg
    async def send_message(self,message,room_name,message_type="text"):
      current_time = time.time()
      if current_time - self.last_message_time < self.message_cooldown:
        return
        
      #檢查訊息是否與上一條訊息相同
      if message == self.last_sent_message:
        return
        
      msg = {
        "username":self.client_name,
        "text":message,
        "room_number":room_name,
        "type":message_type
      }
      await self.sio.emit("chatMessage",message)
      #更新發送時間和消息/訊息
      self.last_message_time = current_time
      self.last_sent_message = message
    async def _on_connect(self):
      print(Fore.GREEN+"已連接伺服器")
      if "on_ready" in self.event_handlers:
        await event_handlers["on_ready"]()
    async def _on_disconnect(self):
      print(Fore.RED+"已斷開連接")
    async def _on_chat_message(self,data):
      username = data.get("username")
      text = data.get("text")
      room_number = data.get("room_number")
      if username == self.client_name:
        return
      print(f"[{room_number}] {username} : {text}")
      #如果有on_message事件處理器，就調用他。
      if "on_message" in self.event_handlers:
        await self.event_handlers["on_message"](username,text,room_number)
    #啟動客戶端
    def run(self):
      loop = asyncio.get_event_loop()
      print(Fore.GREEN+"已連接伺服器")
      loop.run_until_complete(self.connect())
      try:
        loop.run_forever()
      except KeyboardInterrupt:
        print(Fore.RED+"已斷開連接")
        loop.run_until_complete(self.disconnect())
