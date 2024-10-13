import socketio
import asyncio

class Client:
  def __init__(self,client_name):
    self.server_url = "https://sites.wtechhk.xyz"
    self.sio = socketio.AsyncClient
    self.client_name = client_name
    
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
      msg = {
        "username":self.client_name,
        "text":message,
        "room_number":room_name,
        "type":message_type
      }
      
