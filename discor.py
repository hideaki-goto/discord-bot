import discord
import asyncio
import time
from datetime import datetime

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            total = 0
            A = time.time()
            for i in range(1000000):
                total += i
            B = time.time()
            b = format(B-A)
            # メッセージを書きます
            s = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, s + m + b)
    elif message.content.startswith("おつかれ"):
        await client.send_message(message.channel, "hujinami")

@client.event
async def on_message(message):
    if message.content.startswith('$cool'):
        await client.send_message(message.channel, 'Who is cool? Type $name namehere')

        def check(message):
            return message.content.startswith('$name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('$name'):].strip()
        await client.send_message(message.channel, '{} is cool indeed'.format(name))

client.run('NDE1NDExMDUzNDUxNjczNjAx.DW1ksg.KCe27LB5Yw49fPOSj-0MVazboRI')

