# pyzaim
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![logo](/img/pyzaim.svg)

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

## ブランチの運用について

本リポジトリのブランチについては以下の運用といたします。

`master`
- リリース用ブランチ。
- このブランチにマージした時点で新たにタグを打ち、PyPIにアップロードします。
- **このブランチには直接PRを出さないでください。**

`develop`
- 開発用の常駐ブランチ。
- すべてのコミットはこのブランチに一度マージし、動作を確認した上でmasterにマージします。
- PRはこのブランチに対して行ってください。

`feature-*`
- 新規開発用のブランチ。
- 必ずdevelopから分岐し、developにマージする。
- `*`には開発やバグ修正などの対応内容を簡潔に記入。
  - 例: feature-add-headless-mode

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://hackfront.dev"><img src="https://avatars.githubusercontent.com/u/38152917?v=4?s=100" width="100px;" alt=""/><br /><sub><b>りーべ</b></sub></a><br /><a href="#projectManagement-MagicalLiebe" title="Project Management">📆</a> <a href="https://github.com/MagicalLiebe/pyzaim/pulls?q=is%3Apr+reviewed-by%3AMagicalLiebe" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/MagicalLiebe/pyzaim/commits?author=MagicalLiebe" title="Code">💻</a> <a href="https://github.com/MagicalLiebe/pyzaim/commits?author=MagicalLiebe" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Ponk02"><img src="https://avatars.githubusercontent.com/u/24751394?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ponk02</b></sub></a><br /><a href="https://github.com/MagicalLiebe/pyzaim/commits?author=Ponk02" title="Code">💻</a></td>
    <td align="center"><a href="http://zenjiro.wordpress.com/"><img src="https://avatars.githubusercontent.com/u/1298249?v=4?s=100" width="100px;" alt=""/><br /><sub><b>zenjiro</b></sub></a><br /><a href="https://github.com/MagicalLiebe/pyzaim/commits?author=zenjiro" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/omatsu555"><img src="https://avatars.githubusercontent.com/u/40729996?v=4?s=100" width="100px;" alt=""/><br /><sub><b>omatsu555</b></sub></a><br /><a href="https://github.com/MagicalLiebe/pyzaim/commits?author=omatsu555" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/kagemomiji"><img src="https://avatars.githubusercontent.com/u/5343692?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Y.Tory</b></sub></a><br /><a href="https://github.com/MagicalLiebe/pyzaim/commits?author=kagemomiji" title="Code">💻</a></td>
    <td align="center"><a href="https://knoow.jp/@/Omatsu?preview"><img src="https://avatars.githubusercontent.com/u/7794917?v=4?s=100" width="100px;" alt=""/><br /><sub><b>o-matsu</b></sub></a><br /><a href="https://github.com/MagicalLiebe/pyzaim/commits?author=o-matsu" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
