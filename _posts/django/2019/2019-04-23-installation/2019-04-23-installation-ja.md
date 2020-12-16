---
layout: 'post'
permalink: '/django/installation/'
paginate_path: '/django/:num/installation/'
lang: 'ja'
categories: 'django'
comments: true

title: 'ジャンゴ(django)インストール'
description: 'ジャンゴ(django)で開発するためジャンゴ(django)をインストールして設定する方法について説明します。'
image: '/assets/images/category/django/2019/installation/background.jpg'
---

## 概要
パイソン(python)のジャンゴ(django)でサーバーサイドを開発してみようかと思ってました。このブログポストはジャンゴ(django)で開発するためインストールや設定について説明します。

このブログはシリーズです。下記のリンクでシリーズの他の記事を見ることができます。

- ジャンゴ(django)インストール
- [ジャンゴ(django)のプロジェクト開始]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ジャンゴ(django)のモデル(models)の使い方]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [ジャンゴ(django)の管理者ページ]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [ジャンゴ(django)のルーティング(Routing)]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [ジャンゴ(django)のORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [ジャンゴ(django)のビュー(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [ジャンゴ(django)のフォーム(Form)]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [ジャンゴ(django)プロジェクトをヘロク(Heroku)へアップロードする]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

また、このブログシリーズで説明したソースコードはgithubに公開されております。下記のリンクで確認できます。

- github: [https://github.com/dev-yakuza/django_exercise](https://github.com/dev-yakuza/django_exercise){:target="_blank"}

## インストール
ジャンゴ(django)を使うためパイソン(python)をインストールする必要があります。下記のリンクを使って自分のOSに合うパイソン(python)をダウンロードしてインストールします。

- パイソン(python)ダウンロード: [https://www.python.org/downloads/](https://www.python.org/downloads/){:rel="nofollow noreferrer noopener" target="_blank"}

私は主にマック(Mac)を使って開発しています。また、ターミナルは`zsh`を使っています。下記のリンクでマック(Mac)とzshを使ってパイソン(python)を設定する方法を確認してください。

- [マック(Mac)開発環境構築(1) - iTermやzsh]({{site.url}}/environment/mac-iterm-zsh/){:target="_blank"}
- [マック(Mac)開発環境構築(3) - 開発環境]({{site.url}}/environment/mac-development-environment/){:target="_blank"}

上記のリンクでzshとパイソン(python)を設定したら下記のコマンドでバージョンを確認します。

```bash
python --version
Python 3.7.2
```

下記のコマンドでパイソンの仮想環境(Virtual Environment)を簡単に使えるようにしてくれる`virtualenv`モジュールをインストールします。

```bash
pip install virtualenv pylint autopep8
```

下記のコマンドでジャンゴ(django)を使う環境を作ります。

```bash
mkdir server
cd server
virtualenv venv
```

下記のコマンドで仮想環境を実行します。

```bash
source venv/bin/activate
```

下記のコマンドでジャンゴ(django)を仮想環境(Virtual Environment)にインストールします。

```bash
pip install django
```

インストールが終わったら下記のコマンドでジャンゴ(django)がうまくインストールされたか確認します。

```bash
django-admin --version
# 2.2
```

下記のコマンドでインストールした開発環境をファイルで保存します。

```bash
# cd server
pip freeze > requirements.txt
```

インストールが確認できたら下記のコマンドで仮想環境(Virtual Environment)を終了します。

```bash
deactivate
```

また、下記のコマンドを実行して仮想環境(Virtual Environment)が正常に終了されたか確認します。

```bash
django-admin --version
# zsh: command not found: django-admin
```

上のコマンドで仮想環境(Virtual Environment)を理解できると思います。上でインストールしたジャンゴ(django)は仮想環境(Virtual Environment)にインストールしました。したがって、仮想環境(Virtual Environment)が終了された環境でジャンゴ(django)コマンドを実行したらジャンゴ(django)を見つかれませんでしたのエラーが出ます。このようにパイソンの仮想環境(python virtual environment)を使ったらパイソン(python)の開発環境を孤立することができます。

{% include in-feed-ads.html %}

## 他のマシンで使う方法
パイソン(python)の仮想環境(Virtual Environment)は言葉そのまま環境です。したがって、この環境をgitで管理する必要がありません。`.gitignore`に下の内容を追加します。

```bash
# .gitignore
...
venv
```

そしてgitには`requirements.txt`を保存します。他のマシンではgitをクロンして仮想環境はコマンドでインストールします。その後、下記のコマンドでジャンゴ(django)をインストールします。

```bash
# cd server
pip install -r requirements.txt
```

開発する時色んなモジュールをインストールすると思いますが、インストールしたら必ず下記のコマンドで`requirements.txt`を更新します。

```bash
# cd server
pip freeze > requirements.txt
```

## 完了
ジャンゴ(django)を使うためパイソン(python)とパイソンの仮想環境(Virtual Environment)を構成してジャンゴ(django)をインストールして見ました。これでジャンゴ(django)の開発準備ができました。今後はジャンゴを使ってサーバーサイドを開発する方法について説明します。