# 欢迎使用 Lunar_Bot
## 接下来您将跟随设置向导完成设置

---

#### 前情提要
在我们的实际使用中，**Windows（10、11）** 与 **Linux（5.15.0）** 的环境下均正常运行

Python版本建议**3.12+**

如果您的服务器是Linux系统，我们建议您**先**在Windows系统中完成设置，因为这样比较方便，可以使用图形化配置，您也可以参考下方的手动配置教程。

## 部署

---

1. 克隆(Clone)本仓库

```shell
git clone https://github.com/MacroSTAR-Studio/Lunar_Bot.git
```
2. 安装依赖（requirements.txt）

**Important：部分预览版分支的 requirements.txt 可能存在遗漏。如果按照以下操作安装完成后，依然无法使用，你可能需要根据错误信息需要手动安装依赖库。**

(1). 从官方安装
```shell
pip install -r requirements.txt
```
(2).国内服务器可使用清华源或者其他源，例如（例子中使用的是清华源）
```shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
！ 安装 **VC++**

    有一些用户的 Windows 系统中可能没有 ```Visual C++ Redistributable``` 会导致 PySide6 报错：

```
from Shiboken6.Shiboken import
ImportError: DLL load failed while importing Shiboken: 找不到指定的模块
```

可以通过 [安装 Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) 解决此类问题。

请注意，如果您的电脑系统是 Linux 或已经安装 ```Visual C++ Redistributable``` ，则无需重复安装或修复。

## 图形化配置

> [!Note]
> 
> 本图形化部署程序仍在开发，基于Jianer的图形化部署同样适用于Lunar_Bot
> 
> 而且，本分支使用的版本基于Jianer NEXT 3的版本，若包内没有配置向导程序文件，则您需要进一步手动配置。可在后续查看手动配置教程。感谢您对我们工作的理解！

启动设置向导

（基于Windows操作）单击标题栏空白处，输入cmd，回车，输入以下内容

```shell
python SetupWizard.pyw
```

**依次打开设置向导中的每一个页面，完成其中的每一个条目以确保程序能正常运行。**

然后，打开 **核对并应用设置** 页面，点击 **应用** ，看到页面标题显示 “已成功保存” 即表面设置核验无问题，并已经保存。

若出现错误，请浏览下方的设置内容文本框找到报错详细信息，并根据报错提示修改您的配置。

若仍然无法解决，请前往[Issues](https://github.com/MacroSTAR-Studio/Lunar_Bot/issues/new)板块提交您的问题。您需要附上详细的报错内容以及您的步骤，以便于我们分析问题所在

> [!TIP]
> 
> Linux (没有桌面) 的用户可先在 Windows 上启动配置程序,保存配置后将根目录下的 ```appsettings.json``` ```config.json``` 和 ```prerequisites.py``` 复制到服务器即可。

### 手动配置
1. 协议端配置

   创建 或 打开 ```appsettings.json``` 文件，复制以下内容到文件中（如果已有内容则无须复制）

```json
{
    "$schema": "https://raw.githubusercontent.com/LagrangeDev/Lagrange.Core/master/Lagrange.OneBot/Resources/appsettings_schema.json",
    "Logging": {
        "LogLevel": {
            "Default": "Information",
            "Microsoft": "Warning",
            "Microsoft.Hosting.Lifetime": "Information"
        }
    },
    "SignServerUrl": "https://sign.lagrangecore.org/api/sign/30366",
    "SignProxyUrl": "",
    "MusicSignServerUrl": "",
    "Account": {
        "Uin": 2399451783,
        "Protocol": "Linux",
        "AutoReconnect": true,
        "GetOptimumServer": true
    },
    "Message": {
        "IgnoreSelf": true,
        "StringPost": false
    },
    "QrCode": {
        "ConsoleCompatibilityMode": false
    },
    "Implementations": [
        {
            "Type": "ForwardWebSocket",
            "Host": "127.0.0.1",
            "Port": 5004,
            "HeartBeatInterval": 5000,
            "AccessToken": ""
        }
    ]
}
```
找到位于 ```Account``` 下的 ```Uin```，将 ```2221840752``` 替换为你的QQ机器人的QQ号。

2. 机器人配置

    创建 或 打开 ```config.json``` 文件，复制以下内容到文件中（如果已有内容则无须复制）

```json
{
    "owner": [
      2221840752
    ],
    "black_list": [
    ],
    "silents": [
    ],
    "Connection": {
      "mode": "FWS",
      "host": "127.0.0.1",
      "port": 5004,
      "listener_host": "127.0.0.1",
      "listener_port": 5003,
      "retries": 5,
      "satori_token": ""
    },
    "Log_level": "INFO",
    "protocol": "OneBot",
    "Others": {
      "gemini_key": "",
      "openai_key": "",
      "deepseek_key": "",
      "bot_name": "林浅月" ,
      "bot_name_en": "Lunar",
      "ROOT_User": [""],
      "Auto_approval": [""],
      "reminder": "~",
      "slogan": "全能 感知 未来", 
      "TTS": {"voiceColor": "zh-CN-XiaoyiNeural",
              "rate": "+0%",
              "volume": "+0%",
              "pitch": "+0Hz"
          }, 
      "compliment": ["感谢您对{bot_name}的认可"]
      },
      "uin": 0
}
```

更改以下内容
 - ```owner```：替换为你的QQ机器人的QQ号
 - ```black_list```：整数型列表，机器人响应的黑名单。填写在这个列表中的QQ号，其所发送的消息不会被任何模块处理
 - ```Log_level```：日志等级。可选值为DEBUG、TRACE、INFO、WARNING、ERROR、CRITICA（建议日志等级为INFO）
 - ```Others``` ```gemini_key```：使用 Google Gemini 模型的 API KEY
 - ```Others``` ```openai_key```：使用 ChatGPT 模型的 API KEY
 - ```Others``` ```deepseek_key```：使用 Deepseek 模型的 API KEY
 - ```Others``` ```bot_name```：替换为你想给你的机器人取的昵称
 - ```Others``` ```bot_name_en```：替换为你想给你的机器人取的英文昵称
 - ```Others``` ```ROOT_User```：字符串列表。机器人的根用户组，填写根用户组的QQ号。根用户组具有群管的最高权限，同时无法在群聊中更改和删除根用户组。**强烈建议填写你自己的QQ号**
 - ```Others``` ```Auto_approval```：字符串列表。自动审批答案列表。仅在当机器人具有管理员身份时，如果新加群的用户发送的答案存在于该列表之中，则自动同意加群申请
 - ```Others``` ```reminder```：替换为你的机器人的触发关键符号（触发关键词）。如果用户在群聊中发送的消息以该关键词开头，则响应用户消息
 - ```Others``` ```slogan```：替换为你的机器人的宣传标语
 - ```Others``` ```TTS``` ```voiceColor```：EdgeTTS 在生成AI语音回复时所使用的音色
 - ```Others``` ```TTS``` ```rate```：EdgeTTS 在生成AI语音回复时对语速的设定
 - ```Others``` ```TTS``` ```volume```：EdgeTTS 在生成AI语音回复时对音量的设定
 - ```Others``` ```TTS``` ```pitch```：EdgeTTS 在生成AI语音回复时对音调的设定
 - ```Others``` ```compliment```：当用户夸赞机器人时机器人做出的"过激反应"（由于这个功能本身自带的内容太过奇怪，所以我们做了一些小修改）。比如用户发送"{机器人名称}真棒"

3. 定时群发消息配置

    创建 或 打开 ```timing_message.ini``` 文件，复制以下内容到文件中（如果已有内容则无须复制）

```ini
12:00⊕欢迎使用{bot_name}, @{bot_name}查看功能
```

以 ⊕ 作为分隔符，前面的为群发时间（HH:MM），后面的为群发的消息内容。

创建 或 打开 ```blacklist.sr``` 文件，在其中填写定时群发消息屏蔽的群号。一行一个

4. 权限组用户配置

    创建 或 打开 ```Manage_User.ini``` 文件，在其中填写拥有 Manage_User 权限的用户的QQ号。一行一个

    创建 或 打开 ```Super_User.ini``` 文件，在其中填写拥有 Super_User 权限的用户的QQ号。一行一个

## 使用
1. 启动协议端

如果您是 Windows 用户，请双击 ```Lagrange.OneBot.exe```；

如果您是 Linux 用户，请在程序根目录处打开终端，运行
```shell
chmod +x ./Lagrange.OneBot
./Lagrange.OneBot
```

#### 登录协议端

首次打开协议端或者上次退出登录之后需要登录你的QQ账号。

请等待协议端的命令提示符窗口显示一个二维码，立即使用手机进行扫码登录，并勾选**下次自动登录**，即可完成机器人QQ账号绑定。

(若您因为屏幕上的二维码乱码而无法扫描，可前往Lunar_Bot目录寻找一个名为qr-0.png的文件，打开它，然后使用手机摄像头扫描屏幕上的二维码即可授权登录)

#### 退出登录协议端

请关闭简儿和协议端的命令提示符窗口，然后在QQ机器人的根目录下，删除所有 ```.db``` 文件，即算作退出登录。下次启动协议端，请参照上一点进行登录。

2. 启动主程序

在 ```SetupWizard.pyw``` 中打开 **核对并应用设置** 页面，点击 **启动吧，我的简儿！** 即可启动主程序。**注意不要关闭主程序和协议端的命令提示符窗口**

或者，您也可以在程序根目录打开终端，并执行：
```shell
python main.py
```
看到 ℹ️ INFO 成功建立连接 的日志，即表明与协议端对接成功。

# 现在，尽情使用吧！