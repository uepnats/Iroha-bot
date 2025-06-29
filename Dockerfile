FROM python:3.12-slim

# 環境変数を設定（Pythonのログがバッファされず即時表示されるように）
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 最初にライブラリリストをコピーしてインストール
# (こうすると、コード変更のたびにライブラリを再インストールしなくて済む)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD ["python", "main.py"]
