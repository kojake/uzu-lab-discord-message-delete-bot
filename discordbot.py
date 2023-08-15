import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'MTE0MDg3NjAyMDgwNzg5NzE5MA.GZIMI_.CnNnzaq8N7sLaSIZhcUdxL08JR2Xz3KzUBHSt4'

# 必要な Intents を設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容にアクセスするための Intents

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('login success')

#不適切メッセージリスト
Inappropriate_message = [
    "うんこ",
    "ちんこ",
    "",
]

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    #不適切な言葉が入っていないかをチェック
    content = message.content.lower()  # メッセージを小文字に変換して検査
    for word in Inappropriate_message:
        if word in content:
            await message.delete()  # 不適切な言葉が含まれている場合、メッセージを削除
            await message.channel.send(f"{message.author.mention} 不適切な言葉が含まれていたため、メッセージを削除しました。")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
