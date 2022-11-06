# Pythonつかって Slack にメッセージを送る

## 用途

タイトル通りpythonを利用してSlackでメッセージを送信します

## 準備

* pythonが利用できる環境
* `slack_sdk`が利用できる環境
* `python-dotenv`が利用できる環境
* Slack API認証情報

### `slack_sdk`,`python-dotenv`について

`slack_sdk`,`python-dotenv`を利用しているので事前に`pip`または`pip3`でインストールが必要です

```sh
# 例
pip install slack_sdk python-dotenv
```

### Slack API認証情報について

Slackを外部から利用する場合、認証情報が別途必要です。
必要に応じて別途発行してください。必要な情報は、

* SLACK_BOT_TOKEN
* SLACK_APP_TOKEN

となります。

セキュリティの関係上、今回のコードには記載しておらず
`.env`ファイルに以下のような形で記載しています。

```sh:.env
SLACK_BOT_TOKEN="xoxb-00000...xxx"
SLACK_APP_TOKEN="xapp-1-xxx...xxxx"
```

また`.gitignore`で`.env`を追加しているので`git`の追跡対象外にしています。

### 注意事項

Slackではチャンネルごとにメッセージ送信しますので事前にchannelのIDを取得してください
