import os
import discord
from discord import app_commands
from dotenv import load_dotenv

# 最初に一度だけ環境変数を読み込む
load_dotenv()

# calendar_serviceから、設計図であるCalendarServiceクラスをインポート
from calendar_service import CalendarService

# ------------------- 初期設定 -------------------
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# 設計図から、カレンダー担当の執事（インスタンス）を一人作る
try:
    calendar_butler = CalendarService()
except Exception as e:
    print(f"カレンダーサービスの初期化に失敗しました: {e}")
    calendar_butler = None
# ---------------------------------------------


@client.event
async def on_ready():
    print(f'---')
    print(f'{client.user}、ただいま参上いたしました。')
    await tree.sync()
    print(f'旦那様、奥様、いつでもお申し付けください。')
    print(f'---')

# ------------------- コマンド定義 -------------------
@tree.command(name="ping", description="Irohaが挨拶を返します。")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! いつでもお呼びつけください、旦那様、奥様。")

@tree.command(name="schedule", description="カレンダーから直近の予定をお知らせします。")
async def schedule(interaction: discord.Interaction):
    await interaction.response.defer()
    
    if calendar_butler:
        events_text = calendar_butler.get_upcoming_events()
        await interaction.followup.send(events_text)
    else:
        await interaction.followup.send("申し訳ございません。カレンダーサービスが正常に動作しておりません。")
# ---------------------------------------------

# Botを起動
client.run(TOKEN)