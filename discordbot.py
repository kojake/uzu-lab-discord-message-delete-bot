import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

# 必要な Intents を設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容にアクセスするための Intents

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

#不適切メッセージリスト
Inappropriate_message = ["うんこ"]

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content in Inappropriate_message:
        await message.delete()
        await message.channel.send("不適切なメッセージが検知されました")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
