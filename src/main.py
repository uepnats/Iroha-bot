import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True # メッセージの内容を読み取る権限を有効

client = discord.Client(intents=intents)

# スラッシュコマンドを管理するためのツリー
tree = app_commands.CommandTree(client)

# Botが起動したときに実行されるイベント
@client.event
async def on_ready():
    print(f'---')
    print(f'{client.user}、ただいま参上いたしました。')

    # スラッシュコマンドをDiscordに同期
    await tree.sync()

    print(f'旦那様、奥様、いつでもお申し付けください。')
    print(f'---')

# /ping コマンド定義
@tree.command(name="ping", description="Irohaが挨拶を返します")
async def ping(interaction: discord.Interaction):
    """疎通確認用のpingコマンド"""
    await interaction.response.send_message("Pong! いつでもお呼びつけください。")

client.run(TOKEN)