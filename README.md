# WChat

WChat 是一個基於 Socket.IO 的聊天客戶端庫，旨在讓開發者輕鬆地構建實時聊天機器人和應用程序。

## 安裝

要安裝 WChat，請使用以下命令：

```bash
pip install https://github.com/wangtry3417/wtechBot.git
```

引入
```python
from wchat import Client
```

初始化客戶端對象
```python
client_name = 'YourBotUsername'  # 替換為你的機器人用戶名
client = Client(client_name=client_name)
```

註冊事件處理器
```python
@client.on('ready')
async def on_ready():
    print('機器人已準備好！')
    await client.send_message(client_name, 'Hello, world!', 'default')

@client.on('message')
async def on_message(username, msg, room_name):
    print(f'收到消息: [{room_name}] {username}: {msg}')
```

最後，啟動客戶端
``` python
if __name__ == '__main__':
    client.run()
```

All copyright ©️ for W Tech Inc.
