import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

class CalendarService:
    """Googleカレンダーとの連携を担当するクラス"""

    def __init__(self):
        """初期化時に認証情報とサービスを準備する"""
        key_file_path = os.getenv('GOOGLE_KEY_FILE_PATH')
        scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        
        if not key_file_path:
            raise ValueError("環境変数 GOOGLE_KEY_FILE_PATH が設定されていません。")

        # 認証情報を作成
        self.creds = service_account.Credentials.from_service_account_file(key_file_path, scopes=scopes)
        # サービスを構築
        self.service = build('calendar', 'v3', credentials=self.creds)

    def get_upcoming_events(self, max_results=5):
        """Googleカレンダーから直近の予定を取得する"""
        try:
            calendar_id = os.getenv('GOOGLE_CALENDAR_ID')
            if not calendar_id:
                return "環境変数 GOOGLE_CALENDAR_ID が設定されていません。"

            now = datetime.datetime.utcnow().isoformat() + 'Z'
            
            events_result = self.service.events().list(
                calendarId=calendar_id,
                timeMin=now,
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            
            events = events_result.get('items', [])

            if not events:
                return '直近の予定はありません。'

            event_list = "直近の予定はこちらでございますね。\n"
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                start_dt = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))
                start_formatted = start_dt.strftime('%Y年%m月%d日 %H:%M')
                
                event_list += f"- `{start_formatted}`: **{event['summary']}**\n"
            
            return event_list

        except Exception as e:
            print(f"An error occurred: {e}")
            return '申し訳ございません。カレンダーの読み込み中にエラーが発生しました。'