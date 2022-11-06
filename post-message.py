#!/usr/local/bin/python3

from slack_sdk import WebClient
import os
from dotenv import load_dotenv
load_dotenv(override=True)

# 認証情報は.envから取得する
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

# チャンネルはbotを事前に登録しそのIDを指定する必要がある
client = WebClient(token=SLACK_BOT_TOKEN)
response = client.chat_postMessage(channel='C049NP7BY56', text="Pythonから送信")
