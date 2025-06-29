import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True # メッセージの内容を読み取る権限を有効

client = discord.Client(intents=intents)

# Botが起動したときに実行されるイベント
@client.event
async def on_ready():
    print(f'---')
    print(f'{client.user}、ただいま参上いたしました。')
    print(f'旦那様、奥様、いつでもお申し付けください。')
    print(f'---')

client.run(TOKEN)