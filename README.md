# pyzaim

[Zaim](https://zaim.net/)のデータを取得・操作するPythonパッケージ

## 概要

大きくわけて2つの処理を行うパッケージです。

- [Zaim API](https://dev.zaim.net/)のラッパークラス
  - Zaim APIのアクセストークンの発行
  - Rest APIとして提供されている処理の実行
- [Selenium](https://github.com/SeleniumHQ/selenium/tree/master/py)を用いたデータ取得
  - Zaimにはクレジットカードや銀行口座から自動でデータ取得する機能があるが、APIではそれらのデータにはアクセスできない
  - これらの情報を取得するため、Seleniumのwebdriver(Chrome)を用いてデータを取得

## インストール

```bash
pip install pyzaim
```

## 準備

- Zaimアカウントの作成
- Zaim Developersでのアプリケーションの登録 (コンシューマID、コンシューマシークレットの発行)
- Google Chromeおよびseleniumの導入

## 使い方

### Zaim APIのラッパークラスの使い方

- アクセストークンの発行

```python
from pyzaim import get_access_token

get_access_token()

# コンシューマIDとコンシューマシークレットを聞かれるので入力
# 認証ページのURLが表示されるので、アクセスして許可
# 遷移先ページのソースコードから「oauth_verifier」と書いてあるコードをコピーして入力
# 問題なければアクセストークンとアクセスシークレットが表示される
```

- APIを利用してデータを取得・操作

```python
from pyzaim import ZaimAPI

api = ZaimAPI('コンシューマID', 'コンシューマシークレット',
              'アクセストークン', 'アクセスシークレット', 'verifier')

# 動作確認 (ユーザーID等のデータが取得されて、表示されればOK)
print(api.verify())

# データの取得
data = api.get_data()

# 支払いデータの登録
api.insert_payment_simple('日付(datetime.date型)', '金額(int)', 'ジャンル名',
                          '口座名', 'コメント', '品名', '店舗名') # 後半4つは任意入力

# 使用できるジャンル名は以下で確認できる
print(api.genre_itos)

# 使用できる口座名は以下で確認できる
print(api.account_itos)

# 支払いデータの更新 (更新対象データのIDはapi.get_data()で確認)
api.update_payment_simple('更新対象データのID', '日付(datetime.date型)', '金額(int)',
                          'ジャンル名', '口座名', 'コメント', '品名', '店舗名') # 後半4つは任意入力

# 支払いデータの削除
api.delete_payment('削除対象のデータのID')
```

### seleniumを用いたデータ取得

```python
from pyzaim import ZaimCrawler

# Chrome Driverの起動とZaimへのログイン、ログインには少し時間がかかります
crawler = ZaimCrawler('ログインID', 'ログインパスワード',
                    driver_path='Chrome Driverのパス'(PATHが通っていれば省略可),
                    headless=False) # headlessをTrueにするとヘッドレスブラウザで実行できる

# データの取得 (データの取得には少し時間がかかります、時間はデータ件数による)
data = crawler.get_data('取得する年(int)', '取得する月(int)', progress=True) # progressをFalseにするとプログレスバーを非表示にできる

# 終了処理
crawler.close()
```

